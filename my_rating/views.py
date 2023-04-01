from my_rating.serializers import RatingSerializer
from rest_framework.viewsets import ModelViewSet
from my_rating.models import my_Rating


class RatingViewSet(ModelViewSet):
    queryset = my_Rating.objects.all()
    serializer_class = RatingSerializer
    search_fields=('product')
    ordering_fields='__all__'