from store.serializers import StoreSerializer, CommentSerializer, ProductSerializer, CollectionSerializer
from rest_framework.viewsets import ModelViewSet
from store.models import Store, Collection, Product, Comment


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    search_fields = ('owner_phone_number')


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    search_fields = ('store')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ('store')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ('product')
