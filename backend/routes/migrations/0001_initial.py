# Generated by Django 4.2.6 on 2023-10-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("airports", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Route",
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
                ("distance", models.FloatField()),
                ("flight_time", models.DurationField()),
                (
                    "arrival_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="arrival_routes",
                        to="airports.airport",
                    ),
                ),
                (
                    "departure_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departure_routes",
                        to="airports.airport",
                    ),
                ),
            ],
        ),
    ]
