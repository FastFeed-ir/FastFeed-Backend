from rest_framework import serializers
from collection.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
