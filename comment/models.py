from django.db import models
from django.utils import timezone
from product.models import Product


class Comment(models.Model):
    name = models.CharField(max_length=32, default='ناشناس')
    content = models.TextField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} from {self.name} : {self.amount}"
