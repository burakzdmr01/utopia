from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # 🏠 Ana sayfa (ürün listesi + slider)
    path('', views.product_list, name='product_list'),

    # 🎯 Kampanya listesi
    path('campaigns/', views.campaign_list, name='campaign_list'),

    # 🔥 Kampanya detay
    path('campaigns/<int:pk>/', views.campaign_detail, name='campaign_detail'),

    # 🛍️ Ürün detay (slug ile)
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
