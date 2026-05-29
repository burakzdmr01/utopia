from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display  = ('name', 'city', 'phone', 'is_active')
    list_filter   = ('city', 'is_active')
    search_fields = ('name', 'city')
