from django.db import models
from aircrafts.models import Aircraft
from routes.models import Route

class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=255)
    economy_price = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.route} - {self.flight_number}"
