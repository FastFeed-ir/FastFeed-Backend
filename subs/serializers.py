from django.utils import timezone
from rest_framework import serializers
from .models import Store, Subscription


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name')


class SubscriptionSerializer(serializers.ModelSerializer):
    # store = StoreSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ('id', 'store', 'period', 'amount', 'start_date', 'last_extension',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'start_date', 'created_at', 'updated_at')

    def create(self, validated_data):
        object = super().create(validated_data)
        object.created_at = timezone.now()
        object.start_date = object.created_at.date()
        object.last_extension = 0
        object.save()
        return object

    def update(self, instance, validated_data):
        oldCA = instance.created_at
        oldPeriod = instance.period
        oldAmount = instance.amount
        object = super().update(instance, validated_data)
        object.created_at = oldCA
        object.updated_at = timezone.now()
        object.amount = oldAmount + instance.amount
        object.period = oldPeriod + instance.last_extension

        object.save()
        return object
