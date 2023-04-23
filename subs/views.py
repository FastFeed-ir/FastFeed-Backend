from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_id']
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'
