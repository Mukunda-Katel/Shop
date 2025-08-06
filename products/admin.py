from django.contrib import admin
from .models import Category, Product, ProductLike

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'name': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'seller', 'stock', 'available', 'created_at']
    list_filter = ['available', 'category', 'created_at']
    search_fields = ['name', 'description', 'seller__username']
    list_editable = ['price', 'stock', 'available']
    date_hierarchy = 'created_at'

@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'product__name']
