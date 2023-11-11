from django.db import models
from aircrafts.models import Aircraft
from routes.models import Route

class Schedule(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    AircraftID = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    FlightNumber = models.CharField(max_length=255)
    EconomyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Date} - {self.RouteID} - {self.FlightNumber}"
