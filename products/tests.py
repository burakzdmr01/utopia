from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from products.models import Category, Product


class ProductTests(TestCase):

    def setUp(self):
        """Set up test data for product tests."""
        self.client   = Client()
        self.category = Category.objects.create(name='Laptops', slug='laptops-test')
        self.seller   = User.objects.create_user(username='seller_test', password='pass123', role='seller')
        self.product  = Product.objects.create(
            name        = 'MacBook Pro Test',
            slug        = 'macbook-pro-test',
            category    = self.category,
            seller      = self.seller,
            price       = 1999.99,
            stock       = 10,
            description = 'Apple M3 chip',
            is_active   = True
        )

    def test_product_list_page(self):
        """Test that product list page returns 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page(self):
        """Test that product detail page returns 200."""
        response = self.client.get('/macbook-pro-test/')
        self.assertEqual(response.status_code, 200)

    def test_product_search(self):
        """Test that search returns correct product."""
        response = self.client.get('/?q=MacBook')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'MacBook Pro Test')

    def test_product_category_filter(self):
        """Test that category filter works."""
        response = self.client.get('/?category=laptops-test')
        self.assertEqual(response.status_code, 200)

    def test_product_str(self):
        """Test product string representation."""
        self.assertEqual(str(self.product), 'MacBook Pro Test')

    def test_category_str(self):
        """Test category string representation."""
        self.assertEqual(str(self.category), 'Laptops')

    def test_product_discount(self):
        """Test discounted price calculation."""
        self.product.discount = 10
        self.product.save()
        self.assertTrue(self.product.is_on_sale())
        self.assertEqual(self.product.discounted_price(), 1799.99)
