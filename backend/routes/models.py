from django.db import models
from airports.models import Airport

class Route(models.Model):
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_routes')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_routes')
    distance = models.FloatField()
    flight_time = models.DurationField()

    def __str__(self):
        return f"{self.departure_airport} to {self.arrival_airport}"
