from django.db import models
from django.utils import timezone
from owner.models import BusinessOwner
from utilities.constants import BUSINESS_TYPE_CHOICES, STATE_CHOICES


class Store(models.Model):
    title = models.CharField(max_length=32, verbose_name="نام")
    logo = models.ImageField(upload_to='logo_images/', null=True, verbose_name="لوگو(اختیاری)")
    business_type = models.IntegerField(choices=BUSINESS_TYPE_CHOICES, verbose_name="نوع فروشگاه")
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, related_name='stores', verbose_name="مالک فروشگاه")

    state = models.IntegerField(choices=STATE_CHOICES, verbose_name="استان")
    city = models.CharField(max_length=32, null=True, verbose_name="شهر(اختیاری)")
    address = models.CharField(max_length=1024, null=True, blank=True, verbose_name="آدرس(اختیاری)")
    telephone_number = models.CharField(max_length=20, verbose_name = "شماره تلفن")

    tables_count = models.PositiveSmallIntegerField(verbose_name = "تعداد میز")
    subscription_factor = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name = "ضریب اشتراک(اختیاری)")

    instagram_page_link = models.CharField(max_length=32, null=True, blank=True, verbose_name = "آدرس پیج اینستاگرام(اختیاری)")
    telegram_channel_link = models.CharField(max_length=32, null=True, blank=True, verbose_name = "آدرس کانال تلگرام(اختیاری)")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "فروشگاه ها"
        verbose_name = "فروشگاه"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.owner_phone_number = self.business_owner.phone_number
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
