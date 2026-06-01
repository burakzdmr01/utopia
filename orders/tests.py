from django.test import TestCase, Client
from users.models import User
from products.models import Category, Product


class OrderTests(TestCase):

    def setUp(self):
        """Set up test data for order tests."""
        self.client   = Client()
        self.user     = User.objects.create_user(username='customer_test', password='pass123')
        self.category = Category.objects.create(name='Laptops', slug='laptops-order-test')
        self.seller   = User.objects.create_user(username='seller_test2', password='pass123', role='seller')
        self.product  = Product.objects.create(
            name        = 'Test Product',
            slug        = 'test-product',
            category    = self.category,
            seller      = self.seller,
            price       = 999.99,
            stock       = 10,
            description = 'Test description',
            is_active   = True
        )

    def test_cart_requires_login(self):
        """Test that cart page redirects unauthenticated users."""
        response = self.client.get('/orders/cart/')
        self.assertEqual(response.status_code, 302)

    def test_cart_page_logged_in(self):
        """Test that cart page returns 200 for logged in users."""
        self.client.login(username='customer_test', password='pass123')
        response = self.client.get('/orders/cart/')
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        """Test that adding to cart redirects."""
        self.client.login(username='customer_test', password='pass123')
        response = self.client.get(f'/orders/cart/add/{self.product.id}/')
        self.assertEqual(response.status_code, 302)

    def test_checkout_requires_login(self):
        """Test that checkout page redirects unauthenticated users."""
        response = self.client.get('/orders/checkout/')
        self.assertEqual(response.status_code, 302)
