from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo_images/', null=True)
    telephone_number = models.CharField(max_length=20)
    tables_count = models.PositiveSmallIntegerField()
    instagram_page_link = models.CharField(max_length=255)
    telegram_channel_link = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.TextField(null=False, blank=False)
    subscription_factor = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Collection(models.Model):
    title = models.CharField(max_length=255)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='collections')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images/', null=True)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')


class Order(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='orders')
