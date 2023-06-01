from rest_framework import serializers

from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'url', 'business_owner','store_title','end_date')
