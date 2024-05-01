from rest_framework import serializers

from .models import Sensor, SensorData


class SensorSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200)
    description = serializers.CharField()
    owner = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    read_only_fields = ["id", "description", "owner", "created"]


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ["id", "sensor", "data", "created"]
