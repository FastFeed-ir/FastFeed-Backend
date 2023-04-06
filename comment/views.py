from rest_framework.permissions import IsAuthenticated
from comment.serializers import CommentSerializer
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from rating.serializers import RatingSerializer
from rating.models import Rating


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('product')

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    search_fields=('product')
    ordering_fields='__all__'