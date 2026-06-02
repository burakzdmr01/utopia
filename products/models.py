from django.db import models
from decimal import Decimal
from users.models import User


class Category(models.Model):
    parent      = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    name        = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    seller      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name        = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    discount    = models.PositiveIntegerField(default=0, help_text='Discount percentage 0-100')
    stock       = models.PositiveIntegerField(default=0)
    image       = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def discounted_price(self):
        """Returns the price after discount is applied."""
        if self.discount > 0:
            return round(float(self.price) * (1 - self.discount / 100), 2)
        return self.price

    def is_on_sale(self):
        """Returns True if product has an active discount."""
        return self.discount > 0


class Campaign(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    discount    = models.PositiveIntegerField(help_text='Discount percentage')
    products    = models.ManyToManyField(Product, related_name='campaigns')
    image       = models.ImageField(upload_to='campaigns/', blank=True, null=True)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    """Additional images for a product."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image   = models.ImageField(upload_to='products/')
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} — image {self.order}"


class ProductView(models.Model):
    """Tracks product page views."""
    product    = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='views')
    user       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    viewed_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} viewed at {self.viewed_at}"
