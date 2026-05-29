from rest_framework import serializers
from products.models import Product, Category, Campaign
from orders.models import Order, OrderItem
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model  = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'stock', 'is_active', 'category', 'created_at']


class CampaignSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model  = Campaign
        fields = ['id', 'title', 'description', 'discount', 'start_date', 'end_date', 'is_active', 'products']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model  = OrderItem
        fields = ['id', 'product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model  = Order
        fields = ['id', 'status', 'shipping_address', 'total_price', 'created_at', 'items']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'role']
