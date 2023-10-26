from rest_framework.viewsets import ModelViewSet
from .serializers import UserActivitySerializer
from .models import UserActivity

class UserActivityViewset(ModelViewSet):
    queryset=UserActivity.objects.all()
    serializer_class=UserActivitySerializer