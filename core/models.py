from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, verbose_name="نام(اختیاری)")
    last_name = models.CharField(max_length=50, null=True, verbose_name="نام خانوادگی(اختیاری)")
    username = models.CharField(max_length=50, unique=True, verbose_name="نام کاربری")
    password = models.CharField(max_length=50, verbose_name="رمز عبور")


    class Meta:
        verbose_name_plural = "کابران"
        verbose_name = "کاربر"
