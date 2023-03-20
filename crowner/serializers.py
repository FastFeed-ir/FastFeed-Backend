from rest_framework import serializers
from .models import BusinessOwner


class BusinessOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = ['id', 'business_type', 'first_name', 'last_name', 'phone_number', 'updated_at', 'created_at']
        read_only_fields = ('id', 'created_at', 'updated_at')

        def create(self, validated_data):
            object = super().create(validated_data)
            object.created_at = timezone.now()
            object.save()
            return object

        def update(self, instance, validated_data):
            oldCA = instance.created_at
            object = super().update(instance, validated_data)
            object.created_at = oldCA
            object.updated_at = timezone.now()
            object.save()
            return object
