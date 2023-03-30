from .models import BusinessOwner
from .serializers import BusinessOwnerSerializer
from rest_framework.viewsets import ModelViewSet


class BusinessOwnerViewSet(ModelViewSet):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerSerializer
