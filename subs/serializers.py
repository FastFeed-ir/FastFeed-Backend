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
        fields = ('id', 'store', 'period', 'amount', 'start_date', 'end_date', 'past_period', 'remaining', 'extension',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'start_date', 'end_date', 'past_period', 'remaining', 'created_at', 'updated_at')

    # def create(self, validated_data):
    #     store_id = validated_data.get('store')
    #     period = validated_data.get('period')
    #     amount = validated_data.get('amount')
    #     store = Store.objects.get(pk=store_id)
    #     subscription = Subscription(store=store, period=period, amount=amount)
    #     subscription.save()
    #     return subscription

    def update(self, instance, validated_data):
        extension = validated_data.get('extension')
        if extension is not None:
            instance.extend_subscription(extension)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.period = validated_data.get('period', instance.period)
        instance.save()
        return instance
