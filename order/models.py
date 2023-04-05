import random
from django.db import models
from django.utils import timezone
from product.models import Product
from store.models import Store


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders',verbose_name="فروشگاه")
    table_number = models.IntegerField()
    description = models.TextField(max_length=255,null= True,verbose_name="توضیحات سفارش(اختیاری)")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="جمع کل")
    auth_code = models.IntegerField(verbose_name="کد تایید")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.total_amount = 0
            self.auth_code = random.randint(1, 100)
            return super().save(*args, **kwargs)

    def __str__(self):
        return f"از میز {self.table_number} {self.store} به قیمت {self.total_amount} تومان"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="محصول")
    quantity = models.PositiveSmallIntegerField(verbose_name="تعداد")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_Plural = "سفارشات"
        verbose_name = "سفارش"
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            if self.order:
                self.order.total_amount += (self.product.unit_price * self.quantity)
                self.order.save()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def str(self):
        return f"{self.product}:{self.quantity}"
