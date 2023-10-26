from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from .models import Schedule
from .serializers import ScheduleSerializer
from tickets.models import Ticket
from django_filters.rest_framework import DjangoFilterBackend

class ScheduleViewset(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
    'date': ['exact'],
    'flight_number': ['exact', 'icontains'],
    'route__departure_airport__name': ['exact', 'icontains'],
    'route__arrival_airport__name': ['exact', 'icontains'],
}

    @action(detail=True, methods=['get'],permission_classes = [IsAdminUser], url_path="get_price")
    def get_prices(self, request, pk=None):
        # Получение расписания
        schedule = self.get_object()

        # Получение билетов для данного расписания
        tickets = Ticket.objects.filter(schedule=schedule)

        # Подсчет средней цены билетов разных классов
        economy_price = sum(ticket.cabin_type.price for ticket in tickets if ticket.cabin_type.name == 'Economy') / len(tickets)
        business_price = sum(ticket.cabin_type.price for ticket in tickets if ticket.cabin_type.name == 'Business') / len(tickets)
        first_class_price = sum(ticket.cabin_type.price for ticket in tickets if ticket.cabin_type.name == 'First Class') / len(tickets)

        # Добавление информации о ценах в объект расписания
        schedule.economy_price = economy_price
        schedule.business_price = business_price
        schedule.first_class_price = first_class_price

        # Сериализация и возврат данных
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)
    

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser], url_path="cancel_flight")
    def cancel_flight(self, request, pk=None):
        schedule = self.get_object()
        schedule.confirmed = not schedule.confirmed
        schedule.save()
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)
