from rest_framework import serializers
from comment.models import Comment
from rating.models import Rating

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
