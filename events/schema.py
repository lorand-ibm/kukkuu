import graphene
from django.apps import apps
from django.db import transaction
from django.db.models import Count
from django.utils import timezone
from django.utils.translation import get_language
from graphene import Connection, relay
from graphene_django import DjangoConnectionField, DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required, staff_member_required
from graphql_relay import from_global_id

from children.models import Child
from common.utils import update_object, update_object_with_translations
from events.filters import OccurrenceFilter
from events.models import Enrolment, Event, Occurrence
from events.notifications import NotificationType
from events.utils import send_event_notifications_to_guardians
from kukkuu.exceptions import KukkuuGraphQLError
from users.models import Guardian
from venues.models import Venue

EventTranslation = apps.get_model("events", "EventTranslation")


def validate_enrolment(child, occurrence):
    if child.occurrences.filter(event=occurrence.event).exists():
        raise KukkuuGraphQLError("Child already joined this event")
    if occurrence.enrolments.count() >= occurrence.event.capacity_per_occurrence:
        raise KukkuuGraphQLError("Maximum enrolments created")
    if occurrence.time < timezone.now():
        raise KukkuuGraphQLError("Cannot join occurrence in the past")


class EventTranslationType(DjangoObjectType):
    class Meta:
        model = EventTranslation
        exclude = ("id", "master")


class EventNode(DjangoObjectType):
    name = graphene.String()
    description = graphene.String()
    short_description = graphene.String()

    class Meta:
        model = Event
        interfaces = (relay.Node,)

    @classmethod
    @login_required
    # TODO: For now only logged in users can see events
    def get_queryset(cls, queryset, info):
        lang = get_language()
        return queryset.order_by("-created_at").language(lang)

    @classmethod
    @login_required
    def get_node(cls, info, id):
        return super().get_node(info, id)


class EventConnection(Connection):
    class Meta:
        node = EventNode


class OccurrenceNode(DjangoObjectType):
    venue_id = graphene.GlobalID()
    event_id = graphene.GlobalID()
    time = graphene.DateTime()

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        return queryset.order_by("time")

    @classmethod
    @login_required
    def get_node(cls, info, id):
        return super().get_node(info, id)

    class Meta:
        model = Occurrence
        interfaces = (relay.Node,)
        filterset_class = OccurrenceFilter


class EnrolmentNode(DjangoObjectType):
    class Meta:
        model = Enrolment
        interfaces = (relay.Node,)
        fields = ("occurrence", "child", "created_at")


class EventTranslationsInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    short_description = graphene.String()
    description = graphene.String()
    language_code = graphene.String(required=True)


class AddEventMutation(graphene.relay.ClientIDMutation):
    class Input:
        translations = graphene.List(EventTranslationsInput)
        duration = graphene.Int()
        participants_per_invite = graphene.String(required=True)
        capacity_per_occurrence = graphene.Int(required=True)
        image = Upload()

    event = graphene.Field(EventNode)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Add validation
        event = Event.objects.create_translatable_object(**kwargs)
        return AddEventMutation(event=event)


class UpdateEventMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID(required=True)
        duration = graphene.Int()
        participants_per_invite = graphene.String()
        capacity_per_occurrence = graphene.Int()
        image = Upload()
        translations = graphene.List(EventTranslationsInput)
        delete_translations = graphene.List(graphene.String)

    event = graphene.Field(EventNode)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Add validation
        event_global_id = kwargs.pop("id")
        try:
            event = Event.objects.get(pk=from_global_id(event_global_id)[1])
            update_object_with_translations(event, kwargs)
        except Event.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        return UpdateEventMutation(event=event)


class DeleteEventMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID()

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Validate data
        event_id = from_global_id(kwargs["id"])[1]
        try:
            event = Event.objects.get(pk=event_id)
            event.delete()
        except Event.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        return DeleteEventMutation()


class EnrolOccurrenceMutation(graphene.relay.ClientIDMutation):
    class Input:
        occurrence_id = graphene.GlobalID(
            required=True, description="Occurrence id of event"
        )
        child_id = graphene.GlobalID(required=True, description="Guardian's child id")

    enrolment = graphene.Field(EnrolmentNode)

    @classmethod
    @login_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        occurrence_id = from_global_id(kwargs["occurrence_id"])[1]
        child_id = from_global_id(kwargs["child_id"])[1]
        user = info.context.user
        try:
            occurrence = Occurrence.objects.get(pk=occurrence_id)
        except Occurrence.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        try:
            child = Child.objects.user_can_update(user).get(pk=child_id)
        except Child.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        validate_enrolment(child, occurrence)
        enrolment = Enrolment.objects.create(child=child, occurrence=occurrence)

        return EnrolOccurrenceMutation(enrolment=enrolment)


class UnenrolOccurrenceMutation(graphene.relay.ClientIDMutation):
    class Input:
        occurrence_id = graphene.GlobalID(
            required=True, description="Occurrence id " "of event"
        )
        child_id = graphene.GlobalID(required=True, description="Guardian's child id")

    @classmethod
    @login_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        occurrence_id = from_global_id(kwargs["occurrence_id"])[1]
        child_id = from_global_id(kwargs["child_id"])[1]
        user = info.context.user
        try:
            child = Child.objects.user_can_update(user).get(pk=child_id)
        except Child.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        try:
            occurrence = child.occurrences.get(pk=occurrence_id)
            occurrence.children.remove(child)
        except Occurrence.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        return UnenrolOccurrenceMutation()


class AddOccurrenceMutation(graphene.relay.ClientIDMutation):
    class Input:
        time = graphene.DateTime(required=True)
        event_id = graphene.GlobalID(required=True)
        venue_id = graphene.GlobalID(required=True)

    occurrence = graphene.Field(OccurrenceNode)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Validate data
        event_id = from_global_id(kwargs["event_id"])[1]
        try:
            Event.objects.get(pk=event_id)
            kwargs["event_id"] = event_id
        except Event.DoesNotExist as e:
            raise KukkuuGraphQLError(e)

        venue_id = from_global_id(kwargs["venue_id"])[1]
        try:
            Venue.objects.get(pk=venue_id)
            kwargs["venue_id"] = venue_id
        except Venue.DoesNotExist as e:
            raise KukkuuGraphQLError(e)

        occurrence = Occurrence.objects.create(**kwargs)
        return AddOccurrenceMutation(occurrence=occurrence)


class UpdateOccurrenceMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID(required=True)
        time = graphene.DateTime()
        event_id = graphene.GlobalID()
        venue_id = graphene.GlobalID()

    occurrence = graphene.Field(OccurrenceNode)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Validate data
        occurrence_id = from_global_id(kwargs["id"])[1]
        try:
            occurrence = Occurrence.objects.get(pk=occurrence_id)
            kwargs["id"] = occurrence_id
        except Occurrence.DoesNotExist as e:
            raise KukkuuGraphQLError(e)

        if kwargs.get("event_id", None):
            event_id = from_global_id(kwargs["event_id"])[1]
            try:
                Event.objects.get(pk=event_id)
                kwargs["event_id"] = event_id
            except Event.DoesNotExist as e:
                raise KukkuuGraphQLError(e)

        if kwargs.get("venue_id", None):
            venue_id = from_global_id(kwargs["venue_id"])[1]
            try:
                Venue.objects.get(pk=venue_id)
                kwargs["venue_id"] = venue_id
            except Venue.DoesNotExist as e:
                raise KukkuuGraphQLError(e)

        update_object(occurrence, kwargs)
        return UpdateOccurrenceMutation(occurrence=occurrence)


class DeleteOccurrenceMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID(required=True)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Validate data
        occurrence_id = from_global_id(kwargs["id"])[1]
        try:
            occurrence = Occurrence.objects.get(pk=occurrence_id)
            occurrence.delete()
        except Occurrence.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        return DeleteOccurrenceMutation()


class PublishEventMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID(required=True)

    event = graphene.Field(EventNode)

    @classmethod
    @staff_member_required
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **kwargs):
        # TODO: Add validation
        event_global_id = kwargs.pop("id")
        try:
            event = Event.objects.get(pk=from_global_id(event_global_id)[1])
            if event.is_published():
                raise KukkuuGraphQLError("Event is already published")
            event.publish()
            # TODO: Send notifications to guardian who belongs to the same project
            guardians = Guardian.objects.annotate(
                children_count=Count("children")
            ).filter(children_count__gt=0)
            send_event_notifications_to_guardians(
                event, NotificationType.EVENT_PUBLISHED, guardians
            )

        except Event.DoesNotExist as e:
            raise KukkuuGraphQLError(e)
        return PublishEventMutation(event=event)


class Query:
    events = DjangoConnectionField(EventNode)
    occurrences = DjangoFilterConnectionField(OccurrenceNode)

    event = relay.Node.Field(EventNode)
    occurrence = relay.Node.Field(OccurrenceNode)


class Mutation:
    add_event = AddEventMutation.Field()
    update_event = UpdateEventMutation.Field()
    delete_event = DeleteEventMutation.Field()
    publish_event = PublishEventMutation.Field()

    add_occurrence = AddOccurrenceMutation.Field()
    update_occurrence = UpdateOccurrenceMutation.Field()
    delete_occurrence = DeleteOccurrenceMutation.Field()
    enrol_occurrence = EnrolOccurrenceMutation.Field()
    unenrol_occurrence = UnenrolOccurrenceMutation.Field()
