from rest_framework.permissions import IsAuthenticated
from rating.serializers import RatingSerializer
from rest_framework.viewsets import ModelViewSet
from rating.models import my_Rating


class RatingViewSet(ModelViewSet):
    queryset = my_Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    search_fields=('product')
    ordering_fields='__all__'