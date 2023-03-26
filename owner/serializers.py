from rest_framework import serializers
from .models import BusinessOwner


class BusinessOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = ['id', 'business_type', 'first_name', 'last_name', 'phone_number', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_at', 'updated_at')
