from django.db import models
from django.utils import timezone
from product.models import Product


class Comment(models.Model):
    name = models.CharField(max_length=32, default='ناشناس', verbose_name="نام")
    content = models.CharField(max_length=1024, verbose_name="متن نظر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name="محصول")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "نظرات"
        verbose_name = "نظر"


    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} from {self.name} : {self.amount}"



class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, verbose_name="محصول")
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True, verbose_name="امتیاز")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "امتیازات"
        verbose_name = "امتیاز"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.score}'

