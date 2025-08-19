from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "price", "instock_items", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "code", "description")
    readonly_fields = ("created_at", "updated_at")
