# Generated by Django 2.2.13 on 2021-02-04 17:58

from django.db import migrations

import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_add_guardian_languages_spoken_at_home"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.models.UserManager()),
            ],
        ),
    ]
