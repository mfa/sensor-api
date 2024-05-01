from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission

from .models import Sensor


class SensorTokenPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token.lower().startswith("token "):
            token = token.split(" ")[1]
            return Sensor.objects.filter(sensortoken__token=token)
        return False
