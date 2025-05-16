from django.contrib import admin
from accounts.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser',
    )
    list_display_links = (
        'id',
        'phone',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser',
    )
    ordering = ('-id',)
