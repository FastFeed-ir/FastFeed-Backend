from rest_framework.permissions import IsAuthenticated
from order.serializers import OrderSerializer ,OrderItemSerializer
from rest_framework.viewsets import ModelViewSet
from order.models import Order , OrderItem


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
