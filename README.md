# Django Faust Template Repo


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Running this locally

-   Run `docker-compose -f local.yml build` and `docker-compose -f local.yml up broker postgres -d` to start the kafka and postgres containers.

-  Run `docker-compose -f local.yml up django kafka_consumer` to start the django and kafka consumer services.

- If you are running this for the first time, you might have to wait for the kafka service to start before initialising the django and kafka consumer containers. If the kafka service is not up, the django and consumer will crash.


### API
An API has been exposed which consumes data and publishes a message to the kafka service. The consumer will read and persist the body to the DB.

```
curl --location --request POST 'http://localhost:8000/api/v1/metrics/bulk/' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "name": "sree",
        "source":"test",
        "battery_percentage": "45",
        "mobile_make_model": "iphonexr",
        "os_version": "mac_os_sierra",
        "mac_id": "123123",
        "latitude": "19.0536003,",
        "longitude": "73.0828037",
        "timestamp": "2022-10-20T15:58:44.767594+05:30"
    }
]'
```

