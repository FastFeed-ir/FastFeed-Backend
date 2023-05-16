from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Store
from store.serializers import StoreSerializer
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractUser
from store.models import BusinessOwner


class StoreViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john.doe', password='password')  # Create a user
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.business_owner.user = self.user  # Associate the user with the business owner
        self.business_owner.save()
        self.client = APIClient()
        self.store = Store.objects.create(title='Test Store', business_owner=self.business_owner, business_type=1,
                                          owner_phone_number='09123456789', state=1, telephone_number='987654321',
                                          tables_count=5, city='Test City', address='Test Address',
                                          instagram_page_link='test_instagram')

    def test_store_creation(self):
        self.assertEqual(self.store.title, 'Test Store')
        self.assertEqual(self.store.business_owner, self.business_owner)
        self.assertEqual(self.store.business_type, 1)
        self.assertEqual(self.store.owner_phone_number, '09123456789')
        self.assertEqual(self.store.state, 1)
        self.assertEqual(self.store.telephone_number, '987654321')
        self.assertEqual(self.store.tables_count, 5)
        self.assertEqual(self.store.city, 'Test City')
        self.assertEqual(self.store.address, 'Test Address')
        self.assertEqual(self.store.instagram_page_link, 'test_instagram')

    def test_store_serializer(self):
        serializer = StoreSerializer(instance=self.store)
        self.assertEqual(serializer.data['title'], 'Test Store')
        self.assertEqual(serializer.data['business_owner'], self.business_owner.id)
        self.assertEqual(serializer.data['business_type'], 1)
        self.assertEqual(serializer.data['owner_phone_number'], '09123456789')
        self.assertEqual(serializer.data['state'], 1)
        self.assertEqual(serializer.data['telephone_number'], '987654321')
        self.assertEqual(serializer.data['tables_count'], 5)
        self.assertEqual(serializer.data['city'], 'Test City')
        self.assertEqual(serializer.data['address'], 'Test Address')
        self.assertEqual(serializer.data['instagram_page_link'], 'test_instagram')

    def test_store_str_representation(self):
        self.assertEqual(str(self.store), 'Test Store')

    def test_store_update(self):
        new_title = 'Updated Store'
        self.store.title = new_title
        self.store.save()
        updated_store = Store.objects.get(pk=self.store.pk)
        self.assertEqual(updated_store.title, new_title)

    def test_store_deletion(self):
        store_count_before_delete = Store.objects.count()
        self.store.delete()
        store_count_after_delete = Store.objects.count()
        self.assertEqual(store_count_before_delete - 1, store_count_after_delete)

def test_store_retrieval(self):
    url = reverse('store-detail', args=[self.store.id])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    retrieved_store = response.data
    self.assertEqual(retrieved_store['title'], 'Test Store')
    self.assertEqual(retrieved_store['business_owner'], self.business_owner.id)
    self.assertEqual(retrieved_store['business_type'], 1)
    self.assertEqual(retrieved_store['owner_phone_number'], '09123456789')
    self.assertEqual(retrieved_store['state'], 1)
    self.assertEqual(retrieved_store['telephone_number'], '987654321')
    self.assertEqual(retrieved_store['tables_count'], 5)
    self.assertEqual(retrieved_store['city'], 'Test City')
    self.assertEqual(retrieved_store['address'], 'Test Address')
    self.assertEqual(retrieved_store['instagram_page_link'], 'test_instagram')

