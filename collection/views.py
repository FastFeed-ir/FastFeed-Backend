from collection.serializers import CollectionSerializer
from rest_framework.viewsets import ModelViewSet
from collection.models import Collection


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    search_fields = ('store')
