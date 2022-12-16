from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'first_name', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('is_staff', 'user_type', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    list_per_page = 25

admin.site.register(CustomUser, CustomUserAdmin)
