from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from store.models import Store


class Collection(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='collections', verbose_name="فروشگاه")
    title = models.CharField(max_length=31, verbose_name="عنوان")
    is_featured = models.BooleanField(default=False, verbose_name="پیشنهادی بودن(اختیاری)", null=True, blank=True)

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=31, verbose_name="نام")
    unit_price = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="قیمت")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products',
                                   verbose_name="دسته بندی")
    is_available = models.BooleanField(default=True, verbose_name="فعال بودن")
    image = models.TextField(blank=True, verbose_name="تصویر(اختیاری)")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیحات(اختیاری)")
    inventory = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name="تعداد موجود(اختیاری)")
    is_featured = models.BooleanField(default=False, null=True, verbose_name="پیشنهادی بودن(اختیاری)")
    discount_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0.0,
                                              verbose_name="درصد تخفیف(اختیاری)")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, editable=False,
                              verbose_name="فروشگاه(به صورت خودکار افزوده میشود)")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"

    def save(self, *args, **kwargs):
        if not self.id:
            self.store = self.collection.store
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"
