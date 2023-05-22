from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from menu.models import Product
from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_id', 'table_number']
    permission_classes = [IsAuthenticated]


class LastOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, store_id, table_number):
        orders = Order.objects.filter(store_id=store_id, table_number=table_number).order_by('-created_at')
        if orders:
            last_order = orders[0]
            serializer = OrderSerializer(last_order)
            return Response(serializer.data)
        else:
            return Response({'message': 'No orders found for this table.'}, status=404)


class OrderProductIdListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order_items = OrderItem.objects.filter(order_id=order_id)
        if order_items:
            product_ids = [item.product_id for item in order_items]
            return Response({'product_ids': product_ids})
        else:
            return Response({'message': 'No orderItem found for this order.'}, status=404)


class OrderProductNameListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found.'}, status=404)

        order_items = OrderItem.objects.filter(order=order)
        product_ids = [order_item.product_id for order_item in order_items]
        products = Product.objects.filter(id__in=product_ids)
        product_names = [product.title for product in products]

        return Response({'product_names': product_names})


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_id']
    permission_classes = [IsAuthenticated]
