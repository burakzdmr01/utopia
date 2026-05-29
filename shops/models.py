from django.db import models


class Shop(models.Model):
    name          = models.CharField(max_length=200)
    address       = models.TextField()
    city          = models.CharField(max_length=100)
    phone         = models.CharField(max_length=20)
    email         = models.EmailField()
    latitude      = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude     = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image         = models.ImageField(upload_to='shops/', blank=True, null=True)
    is_active     = models.BooleanField(default=True)
    working_hours = models.CharField(max_length=200, default='09:00 - 21:00')

    def __str__(self):
        return f"{self.name} - {self.city}"
