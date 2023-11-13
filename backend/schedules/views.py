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


    @action(detail=True, methods=['get'], permission_classes=[IsAdminUser], url_path="get_prices")
    def get_prices(self, request, pk=None):
        # Получение расписания
        schedule = self.get_object()

        # Получение билетов для данного расписания
        tickets = Ticket.objects.filter(ScheduleID=schedule)

        # Подсчет средней цены билетов разных классов
        economy_prices = [ticket.CabinTypeID.economy_price for ticket in tickets if ticket.CabinTypeID.name == 'Economy']
        business_prices = [ticket.CabinTypeID.economy_price for ticket in tickets if ticket.CabinTypeID.name == 'Business']
        first_class_prices = [ticket.CabinTypeID.economy_price for ticket in tickets if ticket.CabinTypeID.name == 'First Class']

        # Проверка наличия билетов для каждого класса перед вычислением средней цены
        economy_price = sum(economy_prices) / len(economy_prices) if economy_prices else None
        business_price = sum(business_prices) / len(business_prices) if business_prices else None
        first_class_price = sum(first_class_prices) / len(first_class_prices) if first_class_prices else None

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
        schedule.Confirmed = not schedule.Confirmed
        schedule.save()
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)
