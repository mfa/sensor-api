from django.contrib import admin

from .models import Sensor, SensorData, SensorToken


class SensorTokenInline(admin.TabularInline):
    model = SensorToken
    extra = 0


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "owner", "lat", "lon"]
    list_filter = [
        "owner__username",
    ]
    inlines = [
        SensorTokenInline,
    ]


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ["id", "sensor", "data"]
    list_filter = [
        "sensor__id",
        "sensor__owner__username",
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
