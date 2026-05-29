from rest_framework import generics, permissions
from products.models import Product, Category, Campaign
from orders.models import Order
from .serializers import ProductSerializer, CategorySerializer, CampaignSerializer, OrderSerializer


class ProductListAPI(generics.ListAPIView):
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        query    = self.request.query_params.get('q')
        category = self.request.query_params.get('category')
        if query:
            queryset = queryset.filter(name__icontains=query)
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset           = Product.objects.filter(is_active=True)
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field       = 'slug'


class CategoryListAPI(generics.ListAPIView):
    queryset           = Category.objects.all()
    serializer_class   = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CampaignListAPI(generics.ListAPIView):
    queryset           = Campaign.objects.filter(is_active=True)
    serializer_class   = CampaignSerializer
    permission_classes = [permissions.AllowAny]


class OrderListAPI(generics.ListAPIView):
    serializer_class   = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
