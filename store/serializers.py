from rest_framework import serializers
from .models import Store, Collection, Product, Comment


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'title', 'logo', 'telephone_number', 'tables_count',
                  'instagram_page_link', 'telegram_channel_link', 'city',
                  'address', 'subscription_factor', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'store', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'description', 'unit_price', 'inventory',
                  'is_available', 'is_featured', 'discount_percentage',
                  'collection', 'store', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'description', 'created_at', 'product']
        read_only_fields = ['id', 'created_at']
