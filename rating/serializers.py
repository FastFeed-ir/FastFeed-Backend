from rest_framework import serializers
from rating.models import my_Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_Rating
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

