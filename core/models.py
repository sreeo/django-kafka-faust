import datetime

from django.db import models

from model_utils.models import TimeStampedModel, UUIDModel


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):
    class Meta(object):
        abstract = True
