from django.test import TestCase
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime
from menu.models import Collection, Product
from store.models import Store
from django.contrib.auth.models import User
from store.models import BusinessOwner
from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated
from menu.views import CollectionViewSet, ProductViewSet
from decimal import Decimal



class MenuModelsTestCase(TestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John', last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.business_owner.user = self.user
        self.business_owner.save()
        self.store = Store.objects.create(title='Test Store', business_owner=self.business_owner,
                                          business_type=1, owner_phone_number='09123456789', state=1,
                                          telephone_number='987654321', tables_count=5, city='Test City',
                                          address='Test Address', instagram_page_link='test_instagram')

        self.collection = Collection.objects.create(store=self.store, title='Test Collection')
        self.product = Product.objects.create(
            title='Test Product',
            unit_price=10.99,
            collection=self.collection,
            is_available=True
        )

    def test_collection_creation(self):
        now_local = timezone.now()
        now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
        created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        collection = Collection.objects.get(title='Test Collection')

        self.assertEqual(collection.store, self.store)
        self.assertEqual(collection.title, 'Test Collection')
        self.assertEqual(collection.is_featured, False)
        self.assertEqual(collection.created_at, created_at)

    def test_product_creation(self):
        now_local = timezone.now()
        now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
        created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        product = Product.objects.get(title='Test Product')

        self.assertEqual(product.title, 'Test Product')
        self.assertEqual(product.unit_price, Decimal('10.99'))
        self.assertEqual(product.collection, self.collection)
        self.assertEqual(product.is_available, True)
        self.assertEqual(product.created_at, created_at)
        self.assertEqual(product.store, self.store)

    def test_collection_str_representation(self):
        collection = Collection.objects.get(title='Test Collection')
        expected_representation = f"{collection.store}.{collection.title}"
        self.assertEqual(str(collection), expected_representation)

    def test_product_str_representation(self):
        product = Product.objects.get(title='Test Product')
        expected_representation = f"{product.store}.{product.title}"
        self.assertEqual(str(product), expected_representation)

    def test_collection_save_method(self):
        collection = Collection.objects.get(title='Test Collection')
        collection.title = 'Updated Collection'
        collection.save()
        updated_collection = Collection.objects.get(title='Updated Collection')
        self.assertEqual(updated_collection.title, 'Updated Collection')

    def test_product_save_method(self):
        product = Product.objects.get(title='Test Product')
        product.title = 'Updated Product'
        product.save()
        updated_product = Product.objects.get(title='Updated Product')
        self.assertEqual(updated_product.title, 'Updated Product')

    def test_collection_product_relationship(self):
        new_collection = Collection.objects.create(store=self.store, title='New Collection')
        new_product = Product.objects.create(
            title='New Product',
            unit_price=5.99,
            collection=new_collection,
            store=self.store,
        )

        self.assertEqual(new_collection.products.count(), 1)
        self.assertEqual(new_product.collection, new_collection)

    def test_collection_deletion_cascades(self):
        self.store.delete()

        self.assertFalse(Collection.objects.filter(pk=self.collection.pk).exists())
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

    def test_product_store_auto_assignment(self):
        self.assertEqual(self.product.store, self.store)

    def test_permissions_and_authentication(self):
        client = APIClient()
        response = client.post('/collections/', {'store': self.store.pk, 'title': 'New Collection'})
        self.assertEqual(response.status_code, 401)
        client.force_authenticate(user=self.user)  # Force authentication as the user

        response = client.post('/collections/', {'store': self.store.pk, 'title': 'New Collection'})
        self.assertEqual(response.status_code, 201)

        response = client.post('/products/', {'collection': self.collection.pk, 'title': 'New Product'})
        self.assertEqual(response.status_code, 400)


    def test_product_inventory_non_negative(self):
        with self.assertRaises(Exception) as context:
            Product.objects.create(
                title='Negative Inventory Product',
                unit_price=10.99,
                collection=self.collection,
                store=self.store,
                inventory=-1,
            )
        self.assertIn("violates check constraint", str(context.exception))



