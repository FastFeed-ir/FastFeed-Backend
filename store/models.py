from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    logo = models.ImageField(upload_to='logo_images/')
    telephone_number = models.CharField(max_length=20)
    tables_count = models.PositiveSmallIntegerField()
    instagram_page_link = models.CharField(max_length=255)
    telegram_channel_link = models.CharField(max_length=255)
    subscription_factor = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    store = models.OneToOneField(
        Store, on_delete=models.CASCADE, primary_key=True)


class Collection(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    image = models.ImageField(upload_to='products_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def availability(self):
        return self.quantity > 0
    is_available = availability


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
