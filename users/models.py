from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Varsayılan Django kullanıcısını genişletiyoruz.
    3 rol var: admin, seller (satıcı), customer (müşteri)
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('customer', 'Customer'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
