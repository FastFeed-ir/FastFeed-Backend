from django.db.models import Avg
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from menu.models import Product
from .models import Comment, Rating
from .serializers import RatingSerializer, CommentSerializer, OrderCommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_id']
    permission_classes = [IsAuthenticated]


class OrderCommentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if not product_id:
            raise exceptions.ValidationError('Product ID is required.')

        queryset = Comment.objects.filter(order__items__product_id=product_id)

        if not queryset.exists():
            raise exceptions.NotFound('No comments found for the specified product.')

        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except (exceptions.ValidationError, exceptions.NotFound) as e:
            return Response({'detail': str(e)}, status=e.status_code)
        except Exception as e:
            return Response({'detail': 'An error occurred.'}, status=500)


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id']
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'


class ProductRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404("Product not found.")

    def get(self, request, product_id):
        product = self.get_product(product_id)
        try:
            ratings = Rating.objects.filter(product=product)
            rating_count = ratings.count()
            average_rating = ratings.aggregate(Avg('score'))['score__avg']
            average_rating = round(average_rating, 2) if average_rating else None
            data = {
                'average_rating': average_rating,
                'rating_count': rating_count,
            }
            return Response(data)
        except Rating.DoesNotExist:
            raise Http404("No ratings found for this product.")
