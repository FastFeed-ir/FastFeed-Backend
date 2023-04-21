from django.db import models
from django.utils import timezone
from menu.models import Product
from order.models import Order


class Comment(models.Model):
    name = models.CharField(max_length=32, default='ناشناس', verbose_name="نام مشتری")
    content = models.CharField(max_length=1024, verbose_name="متن نظر")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments', verbose_name="سفارش")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "نظرات"
        verbose_name = "نظر"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}:{self.name}"


class Rating(models.Model):
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=1, verbose_name="امتیاز")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "امتیازات"
        verbose_name = "امتیاز"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.score} ستاره'
