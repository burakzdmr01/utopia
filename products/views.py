from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from django.utils import timezone

def product_list(request):
    products   = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(parent=None)  # sadece ana kategoriler

    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    category_slug = request.GET.get('category')
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        # alt kategorileri de dahil et
        subcategories = category.subcategories.all()
        if subcategories:
            products = products.filter(category__in=[category] + list(subcategories))
        else:
            products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page      = request.GET.get('page')
    products  = paginator.get_page(page)

    # Ana sayfa için ekstra veriler
    new_products      = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    campaign_products = Product.objects.filter(is_active=True, campaigns__is_active=True).distinct()[:8]
    campaigns         = Campaign.objects.filter(is_active=True)

    return render(request, 'products/product_list.html', {
        'products':          products,
        'categories':        categories,
        'query':             query,
        'new_products':      new_products,
        'campaign_products': campaign_products,
        'campaigns':         campaigns,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    reviews = product.reviews.all()
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
    })

from .models import Product, Category, Campaign

def campaign_list(request):
    campaigns = Campaign.objects.filter(is_active=True)
    return render(request, 'products/campaign_list.html', {
        'campaigns': campaigns,
    })

def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, is_active=True)
    products = campaign.products.filter(is_active=True)
    return render(request, 'products/campaign_detail.html', {
        'campaign': campaign,
        'products': products,
    })
