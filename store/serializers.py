from rest_framework import serializers
from store.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at','subscription_factor')
