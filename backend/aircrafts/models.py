from django.db import models

class Aircraft(models.Model):
    name = models.CharField(max_length=255)
    make_model = models.CharField(max_length=255)
    total_seats = models.PositiveIntegerField()
    economy_seats = models.PositiveIntegerField()
    business_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name
