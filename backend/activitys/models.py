from django.db import models
from authentication.models import User

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(max_length=255)
    description = models.TextField()