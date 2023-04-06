from rest_framework.permissions import IsAuthenticated
from .serializers import CollectionSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Collection, Product


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('store')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('store')
