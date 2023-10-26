from rest_framework.viewsets import ModelViewSet
from .serializers import RouteSerializer
from .models import Route

class RouteViewset(ModelViewSet):
    queryset=Route.objects.all()
    serializer_class=RouteSerializer