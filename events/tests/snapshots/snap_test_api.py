# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_add_event_staff_user 1"] = {
    "data": {
        "addEvent": {
            "event": {
                "capacityPerOccurrence": 30,
                "duration": 1000,
                "image": "",
                "participantsPerInvite": "FAMILY",
                "publishedAt": None,
                "translations": [
                    {
                        "description": "desc",
                        "languageCode": "FI",
                        "name": "Event test",
                        "shortDescription": "Short desc",
                    }
                ],
            }
        }
    }
}

snapshots["test_add_occurrence_staff_user 1"] = {
    "data": {
        "addOccurrence": {
            "occurrence": {
                "event": {"createdAt": "2020-12-12T00:00:00+00:00"},
                "time": "1986-12-12T16:40:48+00:00",
                "venue": {"createdAt": "2020-12-12T00:00:00+00:00"},
            }
        }
    }
}

snapshots["test_update_event_staff_user 1"] = {
    "data": {
        "updateEvent": {
            "event": {
                "capacityPerOccurrence": 30,
                "duration": 1000,
                "occurrences": {"edges": []},
                "participantsPerInvite": "FAMILY",
                "translations": [
                    {
                        "description": "desc",
                        "languageCode": "SV",
                        "name": "Event test in suomi",
                        "shortDescription": "Short desc",
                    },
                    {
                        "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                        "languageCode": "FI",
                        "name": "Free heart significant machine try.",
                        "shortDescription": "Perform in weight success answer.",
                    },
                ],
            }
        }
    }
}

snapshots["test_staff_publish_event 1"] = {
    "data": {"publishEvent": {"event": {"publishedAt": "2020-12-12T00:00:00+00:00"}}}
}

snapshots["test_occurrence_query_normal_user 1"] = {
    "data": {
        "occurrence": {
            "enrolments": {"edges": []},
            "event": {
                "capacityPerOccurrence": 805,
                "duration": 197,
                "image": "http://testserver/media/spring.jpg",
                "participantsPerInvite": "FAMILY",
                "publishedAt": "2020-12-12T00:00:00+00:00",
                "translations": [
                    {
                        "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                        "languageCode": "FI",
                        "name": "Free heart significant machine try.",
                        "shortDescription": "Perform in weight success answer.",
                    }
                ],
            },
            "remainingCapacity": 805,
            "time": "2020-12-12T00:00:00+00:00",
            "venue": {
                "translations": [
                    {
                        "accessibilityInfo": "Enjoy office water those notice medical. Already name likely behind mission network. Think significant land especially can quite.",
                        "additionalInfo": """Prevent pressure point. Voice radio happen color scene.
Assume training seek full several. Authority develop identify ready.""",
                        "address": """1449 Hill Squares
South Zacharyborough, CO 33337""",
                        "arrivalInstructions": """Last appear experience seven. Throw wrong party wall agency customer clear. Control as receive cup.
Family around year off. Sense person the probably.""",
                        "description": "Later evening southern would according strong. Analysis season project executive entire.",
                        "languageCode": "FI",
                        "name": "Able process base sing according.",
                        "wwwUrl": "http://brooks.org/",
                    }
                ]
            },
        }
    }
}

snapshots["test_update_occurrence_staff_user 1"] = {
    "data": {
        "updateOccurrence": {
            "occurrence": {
                "event": {"createdAt": "2020-12-12T00:00:00+00:00"},
                "time": "1986-12-12T16:40:48+00:00",
                "venue": {"createdAt": "2020-12-12T00:00:00+00:00"},
            }
        }
    }
}

snapshots["test_enrol_occurrence 1"] = {
    "data": {
        "enrolOccurrence": {
            "enrolment": {
                "child": {"firstName": "Alice"},
                "createdAt": "2020-12-12T00:00:00+00:00",
                "occurrence": {"time": "2020-12-12T00:00:00+00:00"},
            }
        }
    }
}

snapshots["test_occurrences_filter_by_date 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {"node": {"time": "1970-01-02T00:00:00+00:00"}},
                {"node": {"time": "1970-01-02T00:00:00+00:00"}},
            ]
        }
    }
}

snapshots["test_occurrences_filter_by_time 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {"node": {"time": "1970-01-01T11:00:00+00:00"}},
                {"node": {"time": "1970-01-02T11:00:00+00:00"}},
            ]
        }
    }
}

snapshots["test_occurrence_available_capacity 1"] = {
    "data": {
        "occurrence": {
            "enrolments": {"edges": []},
            "event": {
                "capacityPerOccurrence": 805,
                "duration": 197,
                "image": "http://testserver/media/spring.jpg",
                "participantsPerInvite": "FAMILY",
                "publishedAt": "2020-12-12T00:00:00+00:00",
                "translations": [
                    {
                        "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                        "languageCode": "EN",
                        "name": "Free heart significant machine try.",
                        "shortDescription": "Perform in weight success answer.",
                    }
                ],
            },
            "remainingCapacity": 802,
            "time": "2020-12-12T00:00:00+00:00",
            "venue": {
                "translations": [
                    {
                        "accessibilityInfo": "Enjoy office water those notice medical. Already name likely behind mission network. Think significant land especially can quite.",
                        "additionalInfo": """Prevent pressure point. Voice radio happen color scene.
Assume training seek full several. Authority develop identify ready.""",
                        "address": """1449 Hill Squares
South Zacharyborough, CO 33337""",
                        "arrivalInstructions": """Last appear experience seven. Throw wrong party wall agency customer clear. Control as receive cup.
Family around year off. Sense person the probably.""",
                        "description": "Later evening southern would according strong. Analysis season project executive entire.",
                        "languageCode": "EN",
                        "name": "Able process base sing according.",
                        "wwwUrl": "http://brooks.org/",
                    }
                ]
            },
        }
    }
}

snapshots["test_enrolment_visibility 1"] = {
    "data": {
        "occurrence": {
            "enrolments": {"edges": [{"node": {"child": {"firstName": "Richard"}}}]},
            "event": {
                "capacityPerOccurrence": 359,
                "duration": 255,
                "image": "http://testserver/media/parent.jpg",
                "participantsPerInvite": "FAMILY",
                "publishedAt": "2020-12-12T00:00:00+00:00",
                "translations": [
                    {
                        "description": """Glass person along age else. Skill down subject town range north skin.
Watch condition like lay still bar later. Daughter order stay sign discover.""",
                        "languageCode": "EN",
                        "name": "Trial western break page box child care. Tv minute defense.",
                        "shortDescription": "Address prove color effort.",
                    }
                ],
            },
            "remainingCapacity": 355,
            "time": "2020-12-12T00:00:00+00:00",
            "venue": {
                "translations": [
                    {
                        "accessibilityInfo": """Data control as receive. End available avoid girl middle.
Sense person the probably. Simply state social believe policy. Score think turn argue present.""",
                        "additionalInfo": "Tough plant traditional after born up always. Return student light a point charge.",
                        "address": """18274 Justin Skyway
Patriciashire, WV 03644""",
                        "arrivalInstructions": "Assume training seek full several. Authority develop identify ready.",
                        "description": """City sing himself yard. Election stay every something base.
Final central situation past ready join enjoy. Huge get this success commercial recently from. Name likely behind mission network who.""",
                        "languageCode": "EN",
                        "name": "Home memory respond improve office table.",
                        "wwwUrl": "http://www.smith-woods.com/",
                    }
                ]
            },
        }
    }
}

snapshots["test_events_query_normal_user 1"] = {
    "data": {
        "events": {
            "edges": [
                {
                    "node": {
                        "capacityPerOccurrence": 805,
                        "createdAt": "2020-12-12T00:00:00+00:00",
                        "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                        "duration": 197,
                        "image": "http://testserver/media/spring.jpg",
                        "name": "Free heart significant machine try.",
                        "occurrences": {
                            "edges": [
                                {
                                    "node": {
                                        "remainingCapacity": 805,
                                        "time": "1986-02-27T01:22:35+00:00",
                                        "venue": {
                                            "translations": [
                                                {
                                                    "description": "Later evening southern would according strong. Analysis season project executive entire.",
                                                    "languageCode": "FI",
                                                    "name": "Subject town range.",
                                                }
                                            ]
                                        },
                                    }
                                }
                            ]
                        },
                        "participantsPerInvite": "FAMILY",
                        "publishedAt": "2020-12-12T00:00:00+00:00",
                        "shortDescription": "Perform in weight success answer.",
                        "translations": [
                            {
                                "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                                "languageCode": "FI",
                                "name": "Free heart significant machine try.",
                                "shortDescription": "Perform in weight success answer.",
                            }
                        ],
                        "updatedAt": "2020-12-12T00:00:00+00:00",
                    }
                }
            ]
        }
    }
}

snapshots["test_event_query_normal_user 1"] = {
    "data": {
        "event": {
            "capacityPerOccurrence": 805,
            "createdAt": "2020-12-12T00:00:00+00:00",
            "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
            "duration": 197,
            "image": "http://testserver/media/spring.jpg",
            "name": "Free heart significant machine try.",
            "occurrences": {
                "edges": [
                    {
                        "node": {
                            "remainingCapacity": 805,
                            "time": "1986-02-27T01:22:35+00:00",
                            "venue": {
                                "translations": [
                                    {
                                        "description": "Later evening southern would according strong. Analysis season project executive entire.",
                                        "languageCode": "FI",
                                        "name": "Subject town range.",
                                    }
                                ]
                            },
                        }
                    }
                ]
            },
            "participantsPerInvite": "FAMILY",
            "publishedAt": "2020-12-12T00:00:00+00:00",
            "shortDescription": "Perform in weight success answer.",
            "translations": [
                {
                    "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                    "languageCode": "FI",
                    "name": "Free heart significant machine try.",
                    "shortDescription": "Perform in weight success answer.",
                }
            ],
            "updatedAt": "2020-12-12T00:00:00+00:00",
        }
    }
}

snapshots["test_occurrences_query_normal_user 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {
                    "node": {
                        "event": {
                            "capacityPerOccurrence": 805,
                            "duration": 197,
                            "image": "http://testserver/media/spring.jpg",
                            "participantsPerInvite": "FAMILY",
                            "publishedAt": "2020-12-12T00:00:00+00:00",
                            "translations": [
                                {
                                    "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                                    "languageCode": "FI",
                                    "name": "Free heart significant machine try.",
                                    "shortDescription": "Perform in weight success answer.",
                                }
                            ],
                        },
                        "remainingCapacity": 805,
                        "time": "2020-12-12T00:00:00+00:00",
                        "venue": {
                            "translations": [
                                {
                                    "accessibilityInfo": "Enjoy office water those notice medical. Already name likely behind mission network. Think significant land especially can quite.",
                                    "additionalInfo": """Prevent pressure point. Voice radio happen color scene.
Assume training seek full several. Authority develop identify ready.""",
                                    "address": """1449 Hill Squares
South Zacharyborough, CO 33337""",
                                    "arrivalInstructions": """Last appear experience seven. Throw wrong party wall agency customer clear. Control as receive cup.
Family around year off. Sense person the probably.""",
                                    "description": "Later evening southern would according strong. Analysis season project executive entire.",
                                    "languageCode": "FI",
                                    "name": "Able process base sing according.",
                                    "wwwUrl": "http://brooks.org/",
                                }
                            ]
                        },
                    }
                }
            ]
        }
    }
}

snapshots["test_occurrences_filter_by_upcoming 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {"node": {"time": "1970-01-01T00:00:00+00:00"}},
                {"node": {"time": "2020-12-12T00:00:00+00:00"}},
            ]
        }
    }
}

snapshots["test_events_query_staff_user 1"] = {
    "data": {
        "events": {
            "edges": [
                {
                    "node": {
                        "capacityPerOccurrence": 805,
                        "createdAt": "2020-12-12T00:00:00+00:00",
                        "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                        "duration": 197,
                        "image": "http://testserver/media/spring.jpg",
                        "name": "Free heart significant machine try.",
                        "occurrences": {
                            "edges": [
                                {
                                    "node": {
                                        "remainingCapacity": 805,
                                        "time": "2009-07-12T04:07:58+00:00",
                                        "venue": {
                                            "translations": [
                                                {
                                                    "description": "Training thought price. Effort clear and local challenge box. Care figure mention wrong when lead involve.",
                                                    "languageCode": "FI",
                                                    "name": "Thank realize staff staff read.",
                                                }
                                            ]
                                        },
                                    }
                                }
                            ]
                        },
                        "participantsPerInvite": "FAMILY",
                        "publishedAt": "2020-12-12T00:00:00+00:00",
                        "shortDescription": "Perform in weight success answer.",
                        "translations": [
                            {
                                "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                                "languageCode": "FI",
                                "name": "Free heart significant machine try.",
                                "shortDescription": "Perform in weight success answer.",
                            }
                        ],
                        "updatedAt": "2020-12-12T00:00:00+00:00",
                    }
                },
                {
                    "node": {
                        "capacityPerOccurrence": 457,
                        "createdAt": "2020-12-12T00:00:00+00:00",
                        "description": """Wonder everything pay parent theory go home. Book and interesting sit future dream party. Truth list pressure stage history.
If his their best. Election stay every something base.""",
                        "duration": 42,
                        "image": "http://testserver/media/think.jpg",
                        "name": "Able process base sing according.",
                        "occurrences": {
                            "edges": [
                                {
                                    "node": {
                                        "remainingCapacity": 457,
                                        "time": "2019-11-11T17:08:21+00:00",
                                        "venue": {
                                            "translations": [
                                                {
                                                    "description": """Along hear follow sometimes. Special far magazine. Know say former conference carry factor front Mr.
Conference thing much like test.""",
                                                    "languageCode": "FI",
                                                    "name": "Hand human value base pattern democratic focus.",
                                                }
                                            ]
                                        },
                                    }
                                }
                            ]
                        },
                        "participantsPerInvite": "FAMILY",
                        "publishedAt": None,
                        "shortDescription": "Later evening southern would according strong.",
                        "translations": [
                            {
                                "description": """Wonder everything pay parent theory go home. Book and interesting sit future dream party. Truth list pressure stage history.
If his their best. Election stay every something base.""",
                                "languageCode": "FI",
                                "name": "Able process base sing according.",
                                "shortDescription": "Later evening southern would according strong.",
                            }
                        ],
                        "updatedAt": "2020-12-12T00:00:00+00:00",
                    }
                },
            ]
        }
    }
}

snapshots["test_occurrences_query_staff_user 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {
                    "node": {
                        "event": {
                            "capacityPerOccurrence": 805,
                            "duration": 197,
                            "image": "http://testserver/media/spring.jpg",
                            "participantsPerInvite": "FAMILY",
                            "publishedAt": "2020-12-12T00:00:00+00:00",
                            "translations": [
                                {
                                    "description": """Serious listen police shake. Page box child care any concern.
Agree room laugh prevent make. Our very television beat at success decade.""",
                                    "languageCode": "FI",
                                    "name": "Free heart significant machine try.",
                                    "shortDescription": "Perform in weight success answer.",
                                }
                            ],
                        },
                        "remainingCapacity": 805,
                        "time": "2020-12-12T00:00:00+00:00",
                        "venue": {
                            "translations": [
                                {
                                    "accessibilityInfo": "Enjoy office water those notice medical. Already name likely behind mission network. Think significant land especially can quite.",
                                    "additionalInfo": """Prevent pressure point. Voice radio happen color scene.
Assume training seek full several. Authority develop identify ready.""",
                                    "address": """1449 Hill Squares
South Zacharyborough, CO 33337""",
                                    "arrivalInstructions": """Last appear experience seven. Throw wrong party wall agency customer clear. Control as receive cup.
Family around year off. Sense person the probably.""",
                                    "description": "Later evening southern would according strong. Analysis season project executive entire.",
                                    "languageCode": "FI",
                                    "name": "Able process base sing according.",
                                    "wwwUrl": "http://brooks.org/",
                                }
                            ]
                        },
                    }
                },
                {
                    "node": {
                        "event": {
                            "capacityPerOccurrence": 700,
                            "duration": 112,
                            "image": "http://testserver/media/send.jpg",
                            "participantsPerInvite": "CHILD_AND_GUARDIAN",
                            "publishedAt": None,
                            "translations": [
                                {
                                    "description": "Expert interview old affect quite nearly gun. Born land military first he law ago. Yard door indicate country individual course.",
                                    "languageCode": "FI",
                                    "name": "Up always sport return. Light a point charge stand store.",
                                    "shortDescription": "East site chance of.",
                                }
                            ],
                        },
                        "remainingCapacity": 700,
                        "time": "2020-12-12T00:00:00+00:00",
                        "venue": {
                            "translations": [
                                {
                                    "accessibilityInfo": """Court possible free anyone floor office eight do. Somebody determine sort under car medical.
Word style also attention word join pay discuss. Performance part prevent explain.""",
                                    "additionalInfo": """Offer organization model remember. Morning culture late oil sell.
Tv news management letter. Animal list adult draw staff her.""",
                                    "address": """663 Keith Ford Apt. 290
Pruitthaven, DE 69289""",
                                    "arrivalInstructions": """Large benefit occur eat discuss quickly buy. Decade address have turn serve me every traditional. Sound describe risk newspaper reflect four.
Six feel real fast.""",
                                    "description": "Run hand human value base. Include and individual effort indeed discuss challenge school. Book significant minute rest two special.",
                                    "languageCode": "FI",
                                    "name": "Huge realize at rather that place against moment.",
                                    "wwwUrl": "https://brown-calhoun.org/",
                                }
                            ]
                        },
                    }
                },
            ]
        }
    }
}

snapshots["test_occurrences_filter_by_venue 1"] = {
    "data": {
        "occurrences": {
            "edges": [
                {"node": {"time": "1989-08-24T14:55:15+00:00"}},
                {"node": {"time": "1990-07-20T12:20:16+00:00"}},
                {"node": {"time": "2017-10-23T18:50:24+00:00"}},
            ]
        }
    }
}
