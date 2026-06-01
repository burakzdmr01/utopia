from django.test import TestCase, Client
from users.models import User


class UserTests(TestCase):

    def setUp(self):
        """Set up test data for user tests."""
        self.client = Client()
        self.user   = User.objects.create_user(username='testuser', password='pass123')

    def test_login_page(self):
        """Test that login page returns 200."""
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """Test that signup page returns 200."""
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """Test that valid login redirects."""
        response = self.client.post('/users/login/', {
            'username': 'testuser',
            'password': 'pass123'
        })
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        """Test that invalid login returns 200 with error."""
        response = self.client.post('/users/login/', {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)

    def test_profile_requires_login(self):
        """Test that profile page redirects unauthenticated users."""
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 302)

    def test_user_str(self):
        """Test user string representation."""
        self.assertEqual(str(self.user), 'testuser (customer)')
