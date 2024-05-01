import secrets

from django.conf import settings
from django.db import models
from ulid import ULID


def ulid_default():
    return str(ULID())


class Sensor(models.Model):
    id = models.CharField(
        max_length=26, primary_key=True, default=ulid_default, editable=False
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    description = models.TextField(default="")
    meta = models.JSONField(
        default=dict, blank=True, help_text="meta information about the sensor"
    )
    # use decimal and add GeoDjango later (if needed)
    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    lon = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    alt = models.DecimalField(
        max_digits=8, decimal_places=3, help_text="in meters", blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.owner}"


def token_default():
    return secrets.token_urlsafe(23)


class SensorToken(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT)
    token = models.CharField(max_length=100, default=token_default)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT)
    data = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)
