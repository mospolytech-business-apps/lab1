from django.forms import model_to_dict
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import datetime, timedelta  # Добавлен импорт для работы с датами
from rest_framework import status

from aircrafts.models import Aircraft
from airoutes.models import Route
from schedules.models import Schedule
from authentication.models import User
from country.models import Country
from airports.models import Airport
from tickets.models import Ticket
from cabintypes.models import CabinType
from tickets.serializers import TicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    outbound_schedules: list[Schedule] = []
    return_schedules: list[Schedule] = []

    def get_value(self, model, key):
        try:
            obj = model_to_dict(model)
            return obj.get(key)
        except Exception as e:
            print("error", e)

    def search_schedule(
        self,
        from_airport: str,
        to_airport: str,
        start_date: datetime,
        end_date: datetime,
        schedules: list[Schedule],
    ):
        from_airport_model = Airport.objects.get(IATACode=from_airport)
        to_airport_model = Airport.objects.get(IATACode=to_airport)

        try:
            route = Route.objects.get(
                DepartureAirport=from_airport_model, ArrivalAirport=to_airport_model
            )
            schedules_query = Schedule.objects.filter(
                Date__range=[start_date, end_date], Route=route
            )

            schedules.extend(
                list(schedules_query)
            )  # Используйте extend для добавления элементов из списка в schedules

        except ObjectDoesNotExist:
            middle_routes = Route.objects.filter(DepartureAirport=from_airport_model)

            for middle_route in middle_routes:
                middle_route_from_airport_id = self.get_value(
                    middle_route, "ArrivalAirport"
                )
                middle_route_from = Airport.objects.get(id=middle_route_from_airport_id)

                try:
                    first_part_route = Route.objects.get(
                        DepartureAirport=from_airport_model,
                        ArrivalAirport=middle_route_from,
                    )
                    second_part_route = Route.objects.get(
                        DepartureAirport=middle_route_from,
                        ArrivalAirport=to_airport_model,
                    )

                    first_part_schedule = Schedule.objects.get(
                        Date__range=[start_date, end_date], Route=first_part_route
                    )
                    second_part_schedule = Schedule.objects.get(
                        Date__range=[start_date, end_date], Route=second_part_route
                    )

                    if first_part_schedule:
                        schedules.append(first_part_schedule)

                    if second_part_schedule:
                        schedules.append(second_part_schedule)
                except ObjectDoesNotExist:
                    return

    @action(methods=["POST"], detail=False, url_path="search")
    def search_flights(self, request):
        from_airport = request.data.get("from_airport")
        to_airport = request.data.get("to_airport")
        cabin_type = request.data.get("cabin_type")
        outbound_date = request.data.get("outbound_date")
        return_date = request.data.get("return_date")
        wide_search = request.data.get("wide_search", False)

        is_economy = cabin_type == "economy"

        def filter_schedule_by_class(schedule: Schedule) -> bool:
            aircraft_id = self.get_value(schedule, "Aircraft")
            aircraft = Aircraft.objects.get(id=aircraft_id)
            economy_seats = self.get_value(aircraft, "EconomySeats")
            business_seats = self.get_value(aircraft, "BusinessSeats")

            if is_economy and economy_seats:
                return True

            if not is_economy and business_seats:
                return True

            return False

        def schedule_adapter(schedules: list[Schedule]):
            result = []

            for schedule in schedules:
                date = self.get_value(schedule, "Date")
                time = self.get_value(schedule, "Time")
                route_id = self.get_value(schedule, "Route")
                route = Route.objects.get(id=route_id)
                departure_airport_id = self.get_value(route, "DepartureAirport")
                arrival_airport_id = self.get_value(route, "ArrivalAirport")
                departure_airport_code = self.get_value(
                    Airport.objects.get(id=departure_airport_id), "IATACode"
                )
                arrival_airport_code = self.get_value(
                    Airport.objects.get(id=arrival_airport_id), "IATACode"
                )

                flight_numbers = [self.get_value(schedule, "FlightNumber")]
                base_price = float(self.get_value(schedule, "EconomyPrice"))

                result.append(
                    {
                        "id": self.get_value(schedule, "id"),
                        "from": departure_airport_code,
                        "to": arrival_airport_code,
                        "date": date,
                        "time": time,
                        "flight_numbers": flight_numbers,
                        "base_price": base_price,
                    }
                )

            return result

        outbound_schedules = []
        return_schedules = []

        try:
            outbound_date_obj = datetime.strptime(outbound_date, "%Y-%m-%d")
            outbound_start_date = (
                outbound_date_obj - timedelta(days=3)
                if wide_search
                else outbound_date_obj
            )
            outbound_end_date = (
                outbound_date_obj + timedelta(days=3)
                if wide_search
                else outbound_date_obj
            )

            self.search_schedule(
                from_airport,
                to_airport,
                outbound_start_date,
                outbound_end_date,
                outbound_schedules,
            )
        except Exception as e:
            return Response({"error": str(e)})

        if return_date:
            try:
                return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")
                return_start_date = (
                    return_date_obj - timedelta(days=3)
                    if wide_search
                    else return_date_obj
                )
                return_end_date = (
                    return_date_obj + timedelta(days=3)
                    if wide_search
                    else return_date_obj
                )

                self.search_schedule(
                    to_airport,
                    from_airport,
                    return_start_date,
                    return_end_date,
                    return_schedules,
                )
            except Exception as e:
                return Response({"error": str(e)})

        outbound_schedules = list(filter(filter_schedule_by_class, outbound_schedules))
        outbound_response = schedule_adapter(outbound_schedules)

        return_response = None

        if return_date:
            return_schedules = list(filter(filter_schedule_by_class, return_schedules))
            return_response = schedule_adapter(return_schedules)

        return Response({"outbound": outbound_response, "returning": return_response})

    @action(methods=["POST"], detail=False, url_path="issue-ticket")
    def confirm_booking(self, request):
        user_id = request.data.get("user")
        schedule_id = request.data.get("schedule")
        cabin_type = request.data.get("cabin_type")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        passport_number = request.data.get("passport_number")
        passport_country_id = request.data.get("passport_country_id")
        booking_reference = request.data.get("booking_reference")
        confirmed = request.data.get("confirmed")

        try:
            user = User.objects.get(id=user_id)
            schedule = Schedule.objects.get(id=schedule_id)
            cabin_type = CabinType.objects.get(name=cabin_type)
            passport_country_id = Country.objects.get(name=passport_country_id).id

            # Создать новый объект билета
            ticket = Ticket.objects.create(
                user=user,
                schedule=schedule,
                cabin_type=cabin_type,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                passport_number=passport_number,
                passport_country_id=passport_country_id,
                booking_reference=booking_reference,
                confirmed=confirmed,
            )

            # Сериализовать билет и вернуть ответ
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
