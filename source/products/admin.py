from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'bean_price',
        'is_active',
    )
    list_display_links = (
        'id',
        'name',
        'description',
        'price',
        'bean_price',
        'is_active',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'code',
    )
    list_display_links = (
        'id',
        'name',
        'code',
    )
