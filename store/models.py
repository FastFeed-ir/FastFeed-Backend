from django.db import models
from django.utils import timezone
from owner.models import BusinessOwner
from utilities.constants import BUSINESS_TYPE_CHOICES, STATE_CHOICES


class Store(models.Model):
    title = models.CharField(max_length=31, verbose_name="نام")
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, related_name='stores',
                                       verbose_name="مالک فروشگاه")
    business_type = models.IntegerField(choices=BUSINESS_TYPE_CHOICES, verbose_name="نوع فروشگاه")
    owner_phone_number = models.CharField(max_length=20, unique=True, verbose_name="شماره تلفن مالک")
    state = models.PositiveIntegerField(choices=STATE_CHOICES, verbose_name="استان")
    telephone_number = models.CharField(max_length=20, verbose_name="شماره تلفن فروشگاه")
    tables_count = models.PositiveSmallIntegerField(verbose_name="تعداد میز")
    logo = models.ImageField(upload_to='logo_images/', blank=True, null=True, verbose_name="لوگو(اختیاری)")

    city = models.CharField(max_length=31, null=True, blank=True, verbose_name="شهر(اختیاری)")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="آدرس(اختیاری)")
    instagram_page_link = models.CharField(max_length=31, null=True, blank=True,
                                           verbose_name="آدرس پیج اینستاگرام(اختیاری)")
    subscription_factor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                              verbose_name="ضریب اشتراک(به صورت خودکار افزوده میشود)")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "فروشگاه ها"
        verbose_name = "فروشگاه"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.owner_phone_number = self.business_owner.phone_number
            self.subscription_factor = 0.0
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
