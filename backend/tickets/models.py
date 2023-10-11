# tickets/models.py

from django.db import models
from authentication.models import User
from schedules.models import Schedule
from countries.models import Country
from сabintyps.models import CabinType  

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    cabin_type = models.ForeignKey(CabinType, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=255)
    passport_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    booking_reference = models.CharField(max_length=255)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.schedule} - {self.first_name} {self.last_name}"
