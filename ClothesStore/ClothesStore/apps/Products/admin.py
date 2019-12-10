from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subcategories._meta.fields]

class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]

class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategories, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(ProductImage)

# admin.site.register(Shoe)
