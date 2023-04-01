from django.db import models
from django.utils import timezone
from store.models import Store
from collection.models import Collection


class Product(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='products_images/', null=True)
    description = models.TextField(null=True)
    unit_price = models.DecimalField(max_digits=15, decimal_places=3)

    inventory = models.PositiveSmallIntegerField(null=True)
    is_available = models.BooleanField(default=False, null=False, blank=False)
    is_featured = models.BooleanField(default=False, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.store = self.collection.store
            return super().save(*args, **kwargs)
        else:
            self.updated_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"