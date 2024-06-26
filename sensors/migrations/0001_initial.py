# Generated by Django 5.0.2 on 2024-05-01 16:18

import django.db.models.deletion
import sensors.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=sensors.models.ulid_default,
                        editable=False,
                        max_length=26,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField(default="")),
                (
                    "meta",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="meta information about the sensor",
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=8, null=True
                    ),
                ),
                (
                    "lon",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=8, null=True
                    ),
                ),
                (
                    "alt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=3,
                        help_text="in meters",
                        max_digits=8,
                        null=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SensorData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.JSONField(blank=True, default=dict)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="sensors.sensor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SensorToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        default=sensors.models.token_default, max_length=100
                    ),
                ),
                ("description", models.CharField(max_length=1000)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="sensors.sensor",
                    ),
                ),
            ],
        ),
    ]
