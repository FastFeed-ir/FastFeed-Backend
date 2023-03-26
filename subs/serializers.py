from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'store', 'period', 'amount', 'start_date',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'start_date', 'created_at', 'updated_at')
