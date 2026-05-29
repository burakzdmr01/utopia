from django.db import models
from users.models import User
from products.models import Product


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE   = 1, '1 Star'
        TWO   = 2, '2 Stars'
        THREE = 3, '3 Stars'
        FOUR  = 4, '4 Stars'
        FIVE  = 5, '5 Stars'

    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product    = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating     = models.IntegerField(choices=Rating.choices)
    comment    = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} — {self.product.name} ({self.rating} stars)"
