from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from owner.models import BusinessOwner
from store.models import Store
from subs.models import Subscription
from subs.serializers import SubscriptionSerializer


class SubscriptionViewSetTestCase(TestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09136534302', first_name='melika',
                                                           last_name='khandan')
        self.user = User.objects.create_user(username='melika.khandan', password='testpass')
        self.token = Token.objects.create(user=self.user)  # Create token for the user
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(title="My Store", business_owner=self.business_owner, business_type=1,
                                          state=1, tables_count=1)

    def test_list_subscriptions(self):
        store = self.store
        Subscription.objects.create(store=store, period=30, amount=100.0)
        response = self.client.get('/subscriptions/')
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)


class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09136534302', first_name='melika',
                                                           last_name='khandan')
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)  # Create token for the user
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(title="My Store", business_owner=self.business_owner, business_type=1,
                                          state=1, tables_count=1)

    def test_create_subscription(self):
        data = {
            'store': self.store.id,
            'period': 30,
            'amount': 100.0
        }
        response = self.client.post('/subscriptions/', data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_subscription(self):
        subscription = Subscription.objects.create(store=self.store, period=30, amount=100.0)
        response = self.client.get(f'/subscriptions/{subscription.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], subscription.id)

    def test_update_subscription(self):
        subscription = Subscription.objects.create(store=self.store, period=30, amount=100.0)
        data = {
            'store': self.store.id,
            'period': 60,
            'amount': 200.0
        }
        response = self.client.patch(f'/subscriptions/{subscription.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['period'], 60)
        self.assertAlmostEqual(float(response.data['amount']), 200.0)

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(store=self.store, period=30, amount=100.0)
        response = self.client.delete(f'/subscriptions/{subscription.id}/')
        self.assertEqual(response.status_code, 204)
