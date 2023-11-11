from django.db import models
from authentication.models import User
from schedules.models import Schedule
from countries.models import Country
from сabintyps.models import CabinType  

class Ticket(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    ScheduleID = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    CabinTypeID = models.ForeignKey(CabinType, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=20)
    PassportNumber = models.CharField(max_length=255)
    PassportCountryID = models.ForeignKey(Country, on_delete=models.CASCADE)
    BookingReference = models.CharField(max_length=255)
    Confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.UserID} - {self.ScheduleID} - {self.FirstName} {self.LastName}"
