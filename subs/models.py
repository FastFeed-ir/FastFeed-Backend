from django.db import models
from store import models as store
from django.utils import timezone


# from store.models import Store

class Subscription(models.Model):
    store = models.ForeignKey(store.Store, on_delete=models.CASCADE)
    period = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateField(auto_now_add=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.start_date=self.created_at.date()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        from django.utils import timezone
        return f"{self.store}.{self.period}day = {self.amount}"
