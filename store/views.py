from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from store.models import Store
from store.serializers import StoreSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('owner_phone_number')
