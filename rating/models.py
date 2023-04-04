from django.db import models
from product.models import Product
from django.utils import timezone
class my_Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.score}'
