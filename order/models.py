from django.db import models
from django.utils import timezone
from store.models import Store
from product.models import Product

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(max_length=255)
    auth_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        else: self.updated_at = timezone.now()
        self.total_amount = sum(item.product.price * item.quantity for item in self.items.all())
        self.auth_code = random.randint(1, 100)
        super(Order, self).save(*args, **kwargs)

    def str(self):
        return f"{self.items} from {self.table_number} : {self.total_amount}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def str(self):
        return f"{self.product}:{self.quantity}"