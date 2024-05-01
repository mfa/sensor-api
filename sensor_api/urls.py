from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import index
from sensors.views import SensorView
from django.urls import include

router = routers.SimpleRouter()
router.register("", SensorView, basename="sensors")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("v1/", include(router.urls)),
]
