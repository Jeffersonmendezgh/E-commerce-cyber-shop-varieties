from django.contrib import admin
from .models import Producto
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "cost", "stock", "is_available", "category", "date_creation")
    prepopulated_fields = {"slug":("name",)}#recordar, sino da error

admin.site.register(Producto, ProductAdmin)