from django.db import models
from django.utils import timezone
from store.models import Store


class Collection(models.Model):
    title = models.CharField(max_length=32, verbose_name="عنوان")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='collections', verbose_name="فروشگاه")
    is_featured = models.BooleanField(default=False, null=True, verbose_name="پیشنهادی بودن(اختیاری)")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=32, verbose_name="نام")
    image = models.ImageField(upload_to='products_images/', blank=True, null=True, verbose_name="تصویر(اختیاری)")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="توضیحات(اختیاری)")
    unit_price = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="قیمت")

    inventory = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="تعداد(اختیاری)")
    is_available = models.BooleanField(default=False, null=False, blank=False, verbose_name="فعال بودن")
    is_featured = models.BooleanField(default=False, null=True, verbose_name="پیشنهادی بودن(اختیاری)")
    discount_percentage = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=0.0,
                                              verbose_name="درصد تخفیف(اختیاری)")

    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name="فروشگاه(به صورت خودکار افزوده میشود)")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products',
                                   verbose_name="دسته بندی")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.store = self.collection.store
            return super().save(*args, **kwargs)
        else:
            self.updated_at = timezone.now()
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"
