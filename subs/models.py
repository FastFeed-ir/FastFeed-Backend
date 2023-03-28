from django.db import models
from store import models as store
from django.utils import timezone
import qrcode
import os
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

directory = os.getenv("QR_CODE_DIR")

class Subscription(models.Model):
    store = models.ForeignKey(store.Store, on_delete=models.CASCADE)
    period = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(null=True, blank=True, max_length=64)

    start_date = models.DateField(auto_now_add=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.start_date = self.created_at.date()
            self.url = f"http://FastFeed.ir/{self.store.business_type}/{self.store.id}/"
            super().save(*args, **kwargs)
            qr_code = qrcode.make(self.url)
            filename = os.path.join(settings.MEDIA_ROOT, directory, f"{self.id}.png")
            qr_code.save(filename)
        else:
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        img_name = f"{self.id}.png"
        img_path = os.path.join(settings.MEDIA_ROOT, directory, img_name)
        if os.path.exists(img_path):
            os.remove(img_path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.period}day = {self.amount}"
