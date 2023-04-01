from rest_framework.viewsets import ModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    search_fields=('store')
    ordering_fields='__all__'