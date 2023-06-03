from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from menu.models import Collection, Product
from order.models import Order
from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer
from django.contrib.auth.models import User
from menu.models import Store
from owner.models import BusinessOwner


class CommentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(
            title='Test Store',
            business_owner=self.business_owner,
            business_type=1,
            state=1,
            telephone_number='987654321',
            tables_count=5,
        )
        self.collection = Collection.objects.create(store=self.store, title='دسته بندی تست')
        self.product = Product.objects.create(is_available=True, unit_price=10.1, inventory=6,
                                              collection=self.collection, title="Product")
        self.order = Order.objects.create(store=self.store, table_number=2)
        self.comment_data = {
            'name': 'John Doe',
            'content': 'This is a comment.',
            'order': self.order,
            'store': self.store,
        }
        self.comment = Comment.objects.create(**self.comment_data)

    def test_create_comment(self):
        self.client = APIClient()
        self.business_owner = BusinessOwner.objects.create(phone_number='0912356789', first_name='John',
                                                           last_name='Doe')
        self.user = User.objects.create_user(username='john.eds', password='ddss')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(
            title='Test Store',
            business_owner=self.business_owner,
            business_type=1,
            state=1,
            telephone_number='987654321',
            tables_count=5,
        )
        self.collection = Collection.objects.create(store=self.store, title='دسته بندی تست')
        self.product = Product.objects.create(is_available=True, unit_price=10.1, inventory=6,
                                              collection=self.collection, title="Product")
        self.order = Order.objects.create(store=self.store, table_number=2)
        self.comment_data = {
            'name': 'John Doe',
            'content': 'This is a comment.',
            'order': self.order.id,
            'store': self.store.id,
        }
        response = self.client.post('/comments/', self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        updated_data = {
            'name': 'Updated Name',
            'content': 'Updated content.',
            'order': self.order.id,
            'store': self.store.id,
        }
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        self.assertEqual(response.data['content'], updated_data['content'])
        self.assertEqual(response.data['order'], updated_data['order'])
        self.assertEqual(response.data['store'], updated_data['store'])

    def test_delete_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)


class CommentSerializerTestCase(TestCase):
    def setUp(self):
        self.comment_data = {
            'content': 'This is a comment.',
            'order': 2,
            'store': 20,
        }
        self.serializer = CommentSerializer(data=self.comment_data)

    # def test_serializer_with_valid_data(self):
    #     self.assertFalse(self.serializer.is_valid())
    #     comment = self.serializer.save()
    #     self.assertEqual(comment.content, self.comment_data['content'])
    #     self.assertIsNone(comment.order)
    #     self.assertIsNone(comment.store)

    # def test_serializer_with_missing_required_fields(self):
    #     invalid_data = {'content': 'This is a comment.'}
    #     serializer = CommentSerializer(data=invalid_data)
    #     self.assertFalse(serializer.is_valid())
    #     self.assertEqual(serializer.errors['order'][0], 'This field is required.')
    #     self.assertEqual(serializer.errors['store'][0], 'This field is required.')


class RatingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(
            title='Test Store',
            business_owner=self.business_owner,
            business_type=1,
            owner_phone_number='09123456789',
            state=1,
            telephone_number='987654321',
            tables_count=5,
            city='Test City',
            address='Test Address',
            instagram_page_link='test_instagram'
        )
        self.collection = Collection.objects.create(store=self.store, title='دسته بندی تست')
        self.product = Product.objects.create(
            title='test',
            is_available=True,
            unit_price=10,
            inventory=6,
            collection=self.collection
        )
        self.rating_data = {
            'score': 4,
            'product': self.product.id,
        }
        self.rating_data1 = {
            'score': 4,
            'product': self.product,
        }
        self.rating = Rating.objects.create(**self.rating_data1)

    def test_create_rating(self):
        url = reverse('rating-list')
        response = self.client.post(url, self.rating_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 2)

    def test_get_rating(self):
        url = reverse('rating-detail', args=[self.rating.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], self.rating_data['score'])

    def test_update_rating(self):
        url = reverse('rating-detail', args=[self.rating.id])
        updated_data = {
            'score': 5,
            'product': self.product.id,
        }
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], updated_data['score'])
        self.assertEqual(response.data['product'], updated_data['product'])

    def test_delete_rating(self):
        url = reverse('rating-detail', args=[self.rating.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Rating.objects.count(), 0)


class RatingSerializerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John',
                                                           last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.store = Store.objects.create(
            title='Test Store',
            business_owner=self.business_owner,
            business_type=1,
            state=1,
            telephone_number='987654321',
            tables_count=5,
        )
        self.collection = Collection.objects.create(store=self.store, title='دسته بندی تست')

        self.product = Product.objects.create(is_available=True, unit_price=10.1, inventory=6,
                                              collection=self.collection, title="Product")
        self.rating_data = {
            'score': 4,
            'product': self.product,
        }
        self.serializer = RatingSerializer(data=self.rating_data)

    def test_serializer_with_missing_required_fields(self):
        invalid_data = {'score': 4}
        serializer = RatingSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
