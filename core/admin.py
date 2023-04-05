from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


@admin.register(User)
class AdminUser(BaseUserAdmin):
    pass
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "password1", "password2",'first_name', 'last_name'),
    #         },
    #     ),
    # )

