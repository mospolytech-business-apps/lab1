from rest_framework import serializers

from schedules.models import Schedule
from aircrafts.models import Aircraft
from airports.models import Airport
from airoutes.models import Route
from aircrafts.serializers import AircraftSerializer
from airoutes.serializers import RouteSerializer

from django.utils.dateparse import parse_date


class ScheduleSerializer(serializers.ModelSerializer):
    Aircraft = AircraftSerializer()
    Route = RouteSerializer()

    class Meta:
        model = Schedule
        fields = "__all__"

    def create(self, validated_data):
        aircraft_data = validated_data.pop("Aircraft")
        aircraft, _ = Aircraft.objects.get_or_create(**aircraft_data)

        route_data = validated_data.pop("Route")
        departure_airport_data = route_data.pop("DepartureAirport")
        arrival_airport_data = route_data.pop("ArrivalAirport")

        departure_airport, _ = Airport.objects.get_or_create(**departure_airport_data)
        arrival_airport, _ = Airport.objects.get_or_create(**arrival_airport_data)

        route, _ = Route.objects.get_or_create(
            DepartureAirport=departure_airport,
            ArrivalAirport=arrival_airport,
            **route_data,
        )

        schedule = Schedule.objects.create(
            Aircraft=aircraft, Route=route, **validated_data
        )

        return schedule

    def update(self, instance, validated_data):
        try:
            instance.Date = validated_data.pop("Date", instance.Date)
            instance.Time = validated_data.pop("Time", instance.Time)
            instance.Aircraft = validated_data.get("Aircraft", instance.Aircraft)
            instance.Route = validated_data.get("Route", instance.Route)
            instance.EconomyPrice = validated_data.get(
                "EconomyPrice", instance.EconomyPrice
            )
            instance.Confirmed = validated_data.get("Confirmed", instance.Confirmed)
            instance.FlightNumber = validated_data.get(
                "FlightNumber", instance.FlightNumber
            )

            instance.save()
            return instance

        except Exception as e:
            print(f"Error in update: {e}")
            raise
