from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from menu.models import Product
from order.models import Order
from store.models import Store


class Comment(models.Model):
    name = models.CharField(max_length=31, default='ناشناس', verbose_name="نام مشتری")
    content = models.CharField(max_length=1023, verbose_name="متن نظر")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='commentsorder', verbose_name="سفارش")
    store = models.ForeignKey(Store, editable=False, on_delete=models.CASCADE, related_name='collectionsstore',
                              verbose_name="فروشگاه(به طور خودکار اضافه میشود)")
    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "نظرات"
        verbose_name = "نظر"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}:{self.name}"


class Rating(models.Model):
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=1, verbose_name="امتیاز")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول", related_name="product")
    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "امتیازات"
        verbose_name = "امتیاز"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.score} ستاره'
