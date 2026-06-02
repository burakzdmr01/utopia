from django.contrib import admin
from .models import Category, Product, Campaign, ProductImage, ProductView

@admin.register(ProductView)
class ProductViewAdmin(admin.ModelAdmin):
    list_display  = ('product', 'user', 'ip_address', 'viewed_at')
    list_filter   = ('viewed_at',)
    search_fields = ('product__name', 'user__username')
    readonly_fields = ('product', 'user', 'ip_address', 'viewed_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'seller', 'price', 'stock', 'is_active')
    list_filter   = ('category', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'is_active')
