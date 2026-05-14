from django.contrib import admin
from .models import Category, Product, Size, ProductImage, ProductSize


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductSizeInline(admin.StackedInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'price')
    list_filter = ('category', 'color')
    search_fields = ('name', 'category', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)