from rest_framework import serializers
from .models import Order, OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        order = validated_data.pop('order')
        order_item = OrderItem.objects.create(order=order, **validated_data)
        order.total_amount += (order_item.product.unit_price * order_item.quantity)
        order.save()
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'total_amount', 'auth_code']
