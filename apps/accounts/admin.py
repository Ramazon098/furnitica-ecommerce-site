from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['email',]
    list_filter = ['email',]

    fieldsets = UserAdmin.fieldsets

    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'first_name', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
