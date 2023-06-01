from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from owner.models import BusinessOwner
from store import models as store


class Subscription(models.Model):
    store = models.ForeignKey(store.Store, on_delete=models.CASCADE, verbose_name="فروشگاه")
    period = models.PositiveIntegerField(verbose_name="دوره زمانی(به روز)")
    amount = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="قیمت کل(به تومان)")
    url = models.CharField(blank=True, max_length=63,
                           verbose_name="آدرس اینترنتی فروشگاه در فست فید(به صورت خودکار افزوده میشود)")

    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, blank=True, null=True, editable=False,
                                       verbose_name="مالک فروشگاه(به صورت خودکار افزوده میشود)")
    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان بروزرسانی")
    end_date = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پایان", editable=False)
    class Meta:
        verbose_name_plural = "اشتراک ها"
        verbose_name = "اشتراک"
    def  calculate_end_date(self):
        now = timezone.now()
        end_date = now + timezone.timedelta(days=self.period)
        return end_date

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
            self.url = f"http://FastFeed.ir/{self.store.business_type}/{self.store.id}/"
            self.business_owner = self.store.business_owner
            self.end_date = self.calculate_end_date()
        else:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.updated_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.period}روز = {self.amount}T"
