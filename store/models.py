from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from owner.models import BusinessOwner
from utilities.constants import BUSINESS_TYPE_CHOICES, STATE_CHOICES


class Store(models.Model):
    title = models.CharField(max_length=31, verbose_name="نام")
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, related_name='stores',
                                       verbose_name="مالک فروشگاه")
    business_type = models.PositiveIntegerField(choices=BUSINESS_TYPE_CHOICES, verbose_name="نوع فروشگاه")
    owner_phone_number = models.CharField(max_length=15, blank=True, editable=False,
                                          verbose_name="شماره تلفن مالک(به صورت خودکار افزوده میشود)")
    state = models.PositiveIntegerField(choices=STATE_CHOICES, verbose_name="استان")
    telephone_number = models.CharField(max_length=15, verbose_name="شماره تلفن فروشگاه")
    tables_count = models.PositiveSmallIntegerField(verbose_name="تعداد میز")
    logo = models.TextField(blank=True, verbose_name="لوگو(اختیاری)")

    city = models.CharField(max_length=31, blank=True, verbose_name="شهر(اختیاری)")
    address = models.CharField(max_length=255, blank=True, verbose_name="آدرس(اختیاری)")
    instagram_page_link = models.CharField(max_length=31, blank=True,
                                           verbose_name="آدرس پیج اینستاگرام(اختیاری)")
    subscription_factor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, editable=False,
                                              verbose_name="ضریب اشتراک(به صورت خودکار افزوده میشود)")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "فروشگاه ها"
        verbose_name = "فروشگاه"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
            self.owner_phone_number = self.business_owner.phone_number
            self.subscription_factor = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
