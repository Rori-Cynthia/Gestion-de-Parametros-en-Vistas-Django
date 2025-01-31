from django.contrib import admin
from .models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'expiration_date', 'manufacturer'
    )
