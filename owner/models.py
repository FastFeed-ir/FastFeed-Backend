from django.db import models
from django.utils import timezone


class BusinessOwner(models.Model):
    CAFE = 'Cafe'
    RESTAURANT = 'Restaurant'
    BUSINESS_TYPE_CHOICES = [
        (CAFE, 'Cafe'),
        (RESTAURANT, 'Restaurant'),
    ]

    business_type = models.CharField(
        max_length=20,
        choices=BUSINESS_TYPE_CHOICES,
        default=RESTAURANT,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
