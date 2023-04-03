from django.db import models
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=255)
    # ...other fields...


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ...other fields...


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Recalculate total_amount every time the Order is saved
        self.total_amount = sum(item.product.price * item.quantity for item in self.items.all())
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
