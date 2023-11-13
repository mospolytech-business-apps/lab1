from django.db import models
from airports.models import Airport

class Route(models.Model):
    DepartureAirportID = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_routes')
    ArrivalAirportID = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_routes')
    Distance = models.FloatField()
    FlightTime = models.DurationField()

    def __str__(self):
        return f"{self.DepartureAirportID} to {self.ArrivalAirportID}"
