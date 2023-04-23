from django.db import models
from django.utils import timezone
from menu.models import Product
from order.models import Order
from store.models import Store


class Comment(models.Model):
    name = models.CharField(max_length=32, default='ناشناس', verbose_name="نام مشتری")
    content = models.CharField(max_length=1024, verbose_name="متن نظر")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='commentsorder', verbose_name="سفارش")
    store = models.ForeignKey(Store, editable=False, on_delete=models.CASCADE, related_name='collectionsstore',
                              verbose_name="فروشگاه(به طور خودکار اضافه میشود)")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "نظرات"
        verbose_name = "نظر"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.store = self.order.store
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}:{self.name}"


class Rating(models.Model):
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=1, verbose_name="امتیاز")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول", related_name="product")
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
