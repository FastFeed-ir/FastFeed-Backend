from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    period = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    past_period = models.PositiveIntegerField(null=True, default=0)
    remaining = models.PositiveIntegerField(default=0, null=True)

    extension = models.PositiveIntegerField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.start_date = self.created_at.date()

        if self.extension:
            self.period += self.extension
            self.updated_at = timezone.now()

        self.end_date = self.start_date + timedelta(days=self.period)
        delta = self.end_date - self.start_date
        self.remaining = delta.days
        self.past_period = self.period - self.remaining

        super().save(*args, **kwargs)

    # def extend_subscription(self, extension):
    #     self.period += extension
    #     self.end_date = self.start_date + timedelta(days=self.period)
    #     delta = self.end_date - self.start_date
    #     self.past_period = delta.days
    #     self.remaining = self.period - self.past_period
    #     self.updated_at = timezone.now()
    #     self.save()
