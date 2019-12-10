from django.contrib import admin
from .models import *
# from Products.models import Product
# Register your models here.
class ProductInline(admin.TabularInline):
    model = ProductinOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Status)
