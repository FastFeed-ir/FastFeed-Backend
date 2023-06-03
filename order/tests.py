from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.urls import reverse
from store import models as store
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from menu.models import Product
from store.models import Store
from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from owner.models import BusinessOwner
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from menu.models import Collection


class OrderTestCase(APITestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.business_owner.user = self.user
        self.business_owner.save()
        self.store = Store.objects.create(title='Test Store', business_owner=self.business_owner,
                                          business_type=1, owner_phone_number='09123456789', state=1,
                                          telephone_number='987654321', tables_count=5, city='Test City',
                                          address='Test Address', instagram_page_link='test_instagram')
        self.collection = Collection.objects.create(store=self.store, title='دسته بندی تست')
        self.product = Product.objects.create(unit_price=10, inventory=6, collection=self.collection)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.order = Order.objects.create(store=self.store, table_number=2)

    def test_create_order(self):
        url = reverse('orders-api')
        data = {
            'store': self.store.id,
            'table_number': 2,
            'order_items': [{'product': self.product.id, 'quantity': 1}],
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(response.data['store'], self.store.id)
        self.assertEqual(response.data['table_number'], 2)
        #self.assertEqual(len(response.data['order_items']), 1)
        # self.assertEqual(response.data['order_items'][0]['product'], self.product.id)
        # self.assertEqual(response.data['order_items'][0]['quantity'], 1)

    def test_list_orders(self):
        url = reverse('orders-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_retrieve_order(self):
    #     url = reverse('orders-api', args=[self.order.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,200)

    # def test_update_order(self):
    #     url = reverse('orders-api', args=[self.order.id])
    #     data = {
    #         'table_number': 3,
    #         'description': 'Updated order description',
    #     }
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code,200)
    #     self.assertEqual(response.data['table_number'], 3)
    #     self.assertEqual(response.data['description'], 'Updated order description')

    # def test_delete_order(self):
    #     url = reverse('order-delete', args=[self.order.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)


class OrderItemTestCase(APITestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.store = Store.objects.create(title='Test Store', business_owner=self.business_owner,
                                          business_type=1, owner_phone_number='09123456789', state=1,
                                          telephone_number='987654321', tables_count=5, city='Test City',
                                          address='Test Address', instagram_page_link='test_instagram')
        self.collection = Collection.objects.create(store=self.store)
        self.product = Product.objects.create(title="product", unit_price=10, inventory=6, collection=self.collection)
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.business_owner.user = self.user
        self.business_owner.save()

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.order = Order.objects.create(store=self.store, table_number=1)
        self.order_item = OrderItem.objects.create(product=self.product, quantity=2, order=self.order)

    def test_list_order_items(self):
        url = reverse('orderitems-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_retrieve_order_item(self):
    #     url = reverse('orderitems-api', args=[self.order_item.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,200)

    def test_create_order_item(self):
        url = reverse('orderitems-api')
        data = {
            'product': self.product.id,
            'quantity': 1,
            'order': self.order.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    # def test_delete_order_item(self):
    #     url = reverse('order-delete', args=[self.order_item.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)

    def test_order_model(self):
        self.assertEqual(self.order.id, 8)
        # add more tests for Order model as needed

    # def test_order_serializer(self):
    #     serializer = OrderSerializer(instance=self.order)
    #     expected_data = {
    #         'id': 1,
    #         'store': self.store.id,
    #         'table_number': 1,
    #         'description': '',
    #     }
    #     self.assertEqual(serializer.data, expected_data)
        # add more tests for OrderSerializer as needed

    def test_order_view(self):
        url = reverse('orderitems-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data), 1)
        # add more tests for OrderViewSet as needed
