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
            self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                               last_name='Doe')
            self.user = User.objects.create_user(username='john.doe', password='password')
            self.business_owner.user = self.user
            self.business_owner.save()
            self.store = Store.objects.create(title='Test Store', business_owner=self.business_owner,
                                              business_type=1, owner_phone_number='09123456789', state=1,
                                              telephone_number='987654321', tables_count=5, city='Test City',
                                              address='Test Address', instagram_page_link='test_instagram')
            self.client = APIClient()
            self.client.force_authenticate(user=self.user)

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

        def test_store_str_representation(self):
            self.assertEqual(str(self.store), 'Test Store')

        def test_store_update(self):
            new_title = 'Updated Store'
            self.store.title = new_title
            self.store.save()
            updated_store = Store.objects.get(pk=self.store.pk)
            self.assertEqual(updated_store.title, new_title)

        def test_store_deletion(self):
            url = reverse('store-detail', args=[self.store.id])
            response = self.client.delete(url)
            self.assertEqual(response.status_code,204)
            self.assertEqual(Store.objects.count(), 0)

        def test_store_retrieval(self):
            url = reverse('store-detail', args=[self.store.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.data['id'], self.store.id)








