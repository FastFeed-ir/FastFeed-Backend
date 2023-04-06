from rest_framework.permissions import IsAuthenticated
from rating.serializers import RatingSerializer
from rest_framework.viewsets import ModelViewSet
from rating.models import Rating


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    search_fields=('product')
    ordering_fields='__all__'