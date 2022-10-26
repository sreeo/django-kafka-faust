from django.db import models

from core.models import TimeStampedUUIDModel


class Metric(TimeStampedUUIDModel):
    name = models.CharField(max_length=256)
    source = models.CharField(max_length=256, null=True)
    timestamp = models.DateTimeField()
    latitude = models.CharField(max_length=16)
    longitude = models.CharField(max_length=16)
    battery_percentage = models.CharField(max_length=16)
    mobile_make_model = models.CharField(max_length=256)
    os_version = models.CharField(max_length=256)
    mac_id = models.CharField(max_length=256)
