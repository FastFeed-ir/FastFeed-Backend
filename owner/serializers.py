from rest_framework import serializers
from .models import BusinessOwner


class BusinessOwnerSerializer(serializers.ModelSerializer):
    # verification_code = serializers.CharField(write_only=True)

    class Meta:
        model = BusinessOwner
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    # def update(self, instance, validated_data):
    #     if instance.verification_code == validated_data.get('verification_code'):
    #         instance.verification_code = None
    #         return super().update(instance, validated_data)
    #     raise serializers.ValidationError("Invalid verification code")
