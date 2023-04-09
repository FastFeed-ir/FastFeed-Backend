import jdatetime
from django.db import models
from django.utils import timezone
from store import models as store
from owner.models import BusinessOwner


class Subscription(models.Model):
    store = models.ForeignKey(store.Store, on_delete=models.CASCADE, verbose_name="فروشگاه")
    period = models.PositiveIntegerField(verbose_name="دوره زمانی(به روز)")
    amount = models.DecimalField(max_digits=20, decimal_places=3, verbose_name="قیمت کل(به تومان)")
    url = models.CharField(null=True, blank=True, max_length=64,
                           verbose_name="آدرس اینترنتی فروشگاه در فست فید(به صورت خودکار افزوده میشود)")

    start_date = models.CharField(null=True, blank=True, verbose_name="تاریخ شروع اشتراک(به صورت خودکار افزوده میشود)",
                                  max_length=10)
    business_owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE,blank=True, null=True,
                                       verbose_name="مالک فروشگاه(به صورت خودکار افزوده میشود)")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "اشتراک ها"
        verbose_name = "اشتراک"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            shamsi_date = jdatetime.date.fromgregorian(date=self.created_at.date())
            self.start_date = shamsi_date.strftime('%Y/%m/%d')
            self.url = f"http://FastFeed.ir/{self.store.business_type}/{self.store.id}/"
            self.business_owner = self.store.business_owner
        else:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.period}روز = {self.amount}T"
