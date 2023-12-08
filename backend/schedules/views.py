import logging
import pandas as pd
import math
from datetime import datetime, time
import csv

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from aircrafts.models import Aircraft
from airports.models import Airport
from aircrafts.serializers import AircraftSerializer
from airoutes.models import Route
from airoutes.serializers import RouteSerializer
from schedules.models import Schedule
from schedules.admin import ScheduleResource
from schedules.serializers import ScheduleSerializer
from rest_framework.exceptions import NotFound


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    @action(
        methods=["PATCH"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="(?P<id>\d+)",
    )
    def update_flight(self, request, id):
        try:
            schedule = Schedule.objects.get(id=id)
        except Schedule.DoesNotExist:
            raise NotFound({"error": "Flight with this id was not found"})

        date = request.data.get("date")
        time = request.data.get("time")
        price = request.data.get("economyPrice")

        if not (date or time or price):
            return Response(
                {"message": "No data provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        if date:
            setattr(schedule, "Date", date)
        if time:
            setattr(schedule, "Time", time)
        if price:
            setattr(schedule, "EconomyPrice", price)

        schedule.save()

        return Response(
            {"message": "Flight updated successfully"}, status=status.HTTP_200_OK
        )

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="cancel/(?P<id>\d+)",
    )
    def cancel_flight(self, request, id):
        try:
            schedule = Schedule.objects.get(id=id)
        except Schedule.DoesNotExist:
            raise NotFound({"error": "Flight with this id was not found"})

        setattr(schedule, "Confirmed", 0)
        schedule.save()

        return Response({"message": "Canceled successfully"})

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="import-csv",
    )
    def import_csv(self, request):
        if request.FILES.get("file"):
            csv_file = request.FILES["file"]

            success_count = 0
            duplicate_count = 0
            missing_fields_count = 0

            content = csv_file.read().decode("utf-8").splitlines()
            reader = csv.reader(content)
            for index, row in enumerate(reader):
                if len(row) < 8:
                    missing_fields_count += 1
                    continue

                try:
                    action = row[0]
                    try:
                        date = datetime.strptime(row[1], "%Y-%m-%d").date()
                        time = datetime.strptime(row[2], "%H:%M").time()
                    except ValueError as e:
                        print(f"Error parsing datetime: {e}")
                        missing_fields_count += 1

                        continue
                    flight_number = row[3]
                    departure_airport = row[4]
                    arrival_airport = row[5]
                    try:
                        aircraft = Aircraft.objects.get(id=int(row[6]))
                    except Aircraft.DoesNotExist:
                        print(f"Invalid aircraft ID: {row[6]} on row {index}")
                        continue
                    economy_price = int(float(row[7]))
                    confirmed = row[8] == "OK"

                    departure_airport_obj = Airport.objects.get(
                        IATACode=departure_airport
                    )
                    arrival_airport_obj = Airport.objects.get(IATACode=arrival_airport)

                    route = Route.objects.filter(
                        DepartureAirport=departure_airport_obj,
                        ArrivalAirport=arrival_airport_obj,
                    ).first()

                except:
                    missing_fields_count += 1
                    continue

                schedule_data = {
                    "Aircraft": {
                        "id": aircraft.id,
                        "Name": aircraft.Name,
                        "MakeModel": aircraft.MakeModel,
                        "TotalSeats": aircraft.TotalSeats,
                        "EconomySeats": aircraft.EconomySeats,
                        "BusinessSeats": aircraft.BusinessSeats,
                    },
                    "Route": {
                        "id": route.id,
                        "DepartureAirport": {
                            "id": route.DepartureAirport.id,
                            "IATACode": route.DepartureAirport.IATACode,
                            "Name": route.DepartureAirport.Name,
                            "CountryID": route.DepartureAirport.CountryID.id,
                        },
                        "ArrivalAirport": {
                            "id": route.ArrivalAirport.id,
                            "IATACode": route.ArrivalAirport.IATACode,
                            "Name": route.ArrivalAirport.Name,
                            "CountryID": route.ArrivalAirport.CountryID.id,
                        },
                        "Distance": route.Distance,
                        "FlightTime": route.FlightTime,
                    },
                    "Confirmed": confirmed,
                    "Date": date,
                    "Time": time,
                    "EconomyPrice": economy_price,
                    "FlightNumber": flight_number,
                }

                duplicated = Schedule.objects.filter(
                    FlightNumber=flight_number, Date=date
                ).first()
                if duplicated:
                    serializer = ScheduleSerializer(duplicated, data=schedule_data)
                    if (
                        duplicated.Aircraft.id == aircraft.id
                        and duplicated.Route.id == route.id
                        and duplicated.Confirmed == bool(confirmed)
                        and duplicated.Date == date
                        and duplicated.Time == time
                        and int(duplicated.EconomyPrice) == int(economy_price)
                        and int(float(duplicated.FlightNumber))
                        == int(float(flight_number))
                    ):
                        duplicate_count += 1
                        continue

                if duplicated and serializer.is_valid() and action == "EDIT":
                    aircraft = Aircraft.objects.get(id=schedule_data["Aircraft"]["id"])
                    route = Route.objects.get(id=schedule_data["Route"]["id"])
                    schedule_data["Aircraft"] = aircraft
                    schedule_data["Route"] = route
                    serializer.update(duplicated, schedule_data)
                    success_count += 1
                    continue

                serializer = ScheduleSerializer(data=schedule_data)
                if serializer.is_valid() and action == "ADD":
                    serializer.save()
                    success_count += 1
                else:
                    print(serializer.errors)

            result = {
                "success_count": success_count,
                "missing_fields_count": missing_fields_count,
                "duplicate_count": duplicate_count,
            }

            return Response(result)

        else:
            return Response(
                {"message": "No CSV file uploaded"}, status=status.HTTP_400_BAD_REQUEST
            )
