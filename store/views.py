from store.serializers import StoreSerializer, CommentSerializer, ProductSerializer, CollectionSerializer
from rest_framework.viewsets import ModelViewSet
from store.models import Store, Collection, Product, Comment


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
