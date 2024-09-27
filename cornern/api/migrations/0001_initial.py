# Generated by Django 5.1.1 on 2024-09-27 11:37

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Corner",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
                (
                    "loudness",
                    models.CharField(
                        choices=[
                            ("Sehr laut", "Veryloud"),
                            ("Laut", "Loud"),
                            ("neutral", "Neutral"),
                            ("leise", "Quiet"),
                            ("Sehr leise", "Veryquiet"),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "corner",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.corner"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sensor",
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
                ("name", models.CharField(max_length=100)),
                ("token", models.UUIDField(default=uuid.uuid4)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "corner",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.corner"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
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
                ("value", models.IntegerField()),
                ("prediction", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "sensor",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.sensor"),
                ),
            ],
        ),
    ]
