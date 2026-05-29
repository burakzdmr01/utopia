from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPI.as_view(), name='api_products'),
    path('products/<slug:slug>/', views.ProductDetailAPI.as_view(), name='api_product_detail'),
    path('categories/', views.CategoryListAPI.as_view(), name='api_categories'),
    path('campaigns/', views.CampaignListAPI.as_view(), name='api_campaigns'),
    path('orders/', views.OrderListAPI.as_view(), name='api_orders'),
]
