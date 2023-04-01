from django.db import models
from store.models import Store , Product
import random
from django.utils import timezone
class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    products = models.JSONField()
    table_number = models.PositiveSmallIntegerField()
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    description = models.TextField(max_length=255)
    auth_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        else: self.updated_at = timezone.now()
        total = 0.00
        for product_id, quantity in self.products.items():
            product = Product.objects.get(pk=product_id)
            total += product.unit_price * quantity
        self.total_amount = total
        self.auth_code = random.randint(1, 100)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.products} from {self.table_number} : {self.total_amount}"