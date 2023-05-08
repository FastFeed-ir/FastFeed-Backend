from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_id', 'table_number']
    permission_classes = [IsAuthenticated]


class LastOrderView(APIView):
    def get(self, request, store_id, table_number):
        orders = Order.objects.filter(store_id=store_id, table_number=table_number).order_by('-created_at')
        if orders:
            last_order = orders[0]
            serializer = OrderSerializer(last_order)
            return Response(serializer.data)
        else:
            return Response({'message': 'No orders found for this table.'}, status=404)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_id']
    permission_classes = [IsAuthenticated]
