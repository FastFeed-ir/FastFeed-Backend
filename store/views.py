from store.serializers import StoreSerializer
from rest_framework.viewsets import ModelViewSet
from store.models import Store


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    search_fields = ('owner_phone_number')
