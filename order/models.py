import random

from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from menu.models import Product
from store.models import Store


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders', verbose_name="فروشگاه")
    table_number = models.PositiveSmallIntegerField(verbose_name="میز")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیحات سفارش(اختیاری)")
    auth_code = models.IntegerField(blank=True, verbose_name="کد احرازهویت(به صورت خودکار افزوده میشود)")
    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت سفارش")

    class Meta:
        verbose_name_plural = "سفارشات"
        verbose_name = "سفارش"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
            self.auth_code = random.randint(100, 999)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"میز {self.table_number} {self.store} {self.created_at}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    product_title = models.CharField(max_length=31, blank=True, editable=False,
                                     verbose_name="نام محصول(به صورت خودکار افزوده میشود)")
    product_unit_price = models.DecimalField(max_digits=15, blank=True, editable=False, decimal_places=3,
                                             verbose_name="قیمت محصول(به صورت خودکار افزوده میشود)")
    quantity = models.PositiveSmallIntegerField(verbose_name="تعداد")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="سفارش")
    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت ")

    class Meta:
        verbose_name_plural = "آیتم های سفارش"
        verbose_name = "آیتم سفارش"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
            self.product_title = self.product.title
            self.product_unit_price = self.product.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product}:{self.quantity}"
