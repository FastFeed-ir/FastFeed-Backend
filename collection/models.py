from django.db import models
from django.utils import timezone
from store.models import Store


class Collection(models.Model):
    title = models.CharField(max_length=32, verbose_name="نام")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='collections', verbose_name="فروشگاه")
    is_featured = models.BooleanField(default=False, null=True, verbose_name="پیشنهادی(اختیاری)")

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
