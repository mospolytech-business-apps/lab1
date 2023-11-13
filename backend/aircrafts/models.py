from django.db import models

class Aircraft(models.Model):
    Name = models.CharField(max_length=255)
    MakeModel = models.CharField(max_length=255)
    TotalSeats = models.PositiveIntegerField()
    EconomySeats = models.PositiveIntegerField()
    BusinessSeats = models.PositiveIntegerField()

    def __str__(self):
        return self.Name
