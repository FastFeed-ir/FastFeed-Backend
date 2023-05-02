from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.urls import reverse
from store import models as store
class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.store = store.Store.objects.create(title='فروشگاه تست', address='آدرس تست')
        self.order = Order.objects.create(store=self.store, table_number=1, description='توضیحات تست')

    def test_order_model(self):
        self.assertEqual(self.order.id, 1)
        # add more tests for Order model as needed

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        expected_data = {
            'id': 1,
            'store': self.store.id,
            'table_number': 1,
            'description': 'توضیحات تست',
        }
        self.assertEqual(serializer.data, expected_data)
        # add more tests for OrderSerializer as needed

    def test_order_view(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # add more tests for OrderViewSet as needed