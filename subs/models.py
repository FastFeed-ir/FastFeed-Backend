from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# from store.models import Store

class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True)
    period = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_extension = models.PositiveIntegerField(null=True)

    start_date = models.DateField(auto_now_add=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField( null=True, blank=True)

