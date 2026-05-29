from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from products.models import Product

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        Review.objects.update_or_create(
            user=request.user,
            product=product,
            defaults={
                'rating':  request.POST.get('rating'),
                'comment': request.POST.get('comment'),
            }
        )
    return redirect('products:product_detail', slug=product.slug)
