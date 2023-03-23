from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.serializers import StoreSerializer, CommentSerializer, ProductSerializer, CollectionSerializer
from rest_framework.viewsets import ModelViewSet
from store.models import Store, Collection, Product, Comment


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentSerializer(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
