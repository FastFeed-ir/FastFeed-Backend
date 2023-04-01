from order.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet
from order.models import Order


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer