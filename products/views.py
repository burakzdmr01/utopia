from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Product, Category, Campaign, ProductView
import requests as req


def get_exchange_rates():
    """
    Fetches live exchange rates from ExchangeRate-API.
    Returns EUR, GBP, and TRY rates relative to USD.
    Falls back to static rates if the API is unavailable.
    """
    try:
        response = req.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=5)
        data = response.json()
        print("API rates:", data['rates']['EUR'], data['rates']['GBP'], data['rates']['TRY'])
        return {
            'EUR': round(data['rates']['EUR'], 2),
            'GBP': round(data['rates']['GBP'], 2),
            'TRY': round(data['rates']['TRY'], 2),
        }
    except Exception as e:
        print("API error:", e)
        return {'EUR': 0.92, 'GBP': 0.79, 'TRY': 32.5}

def product_list(request):
    """
    Displays the main product listing page.
    Supports search by name and filtering by category slug.
    Also provides data for the homepage (new arrivals, campaigns, hot deals).
    """
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(parent=None)

    # Search filter
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Category filter — includes subcategories
    category_slug = request.GET.get('category')
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        subcategories = category.subcategories.all()
        if subcategories:
            products = products.filter(category__in=[category] + list(subcategories))
        else:
            products = products.filter(category=category)

    # Pagination — 18 products per page
    paginator = Paginator(products, 18)
    page      = request.GET.get('page')
    products  = paginator.get_page(page)

    # Homepage extras
    new_products      = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    campaign_products = Product.objects.filter(is_active=True, campaigns__is_active=True).distinct()[:8]
    campaigns = Campaign.objects.all()

    return render(request, 'products/product_list.html', {
        'products':          products,
        'categories':        categories,
        'query':             query,
        'new_products':      new_products,
        'campaign_products': campaign_products,
        'campaigns':         campaigns,
    })

def product_detail(request, slug):
    """Displays a single product's detail page."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    reviews = product.reviews.all()
    rates   = get_exchange_rates()

    # Görüntülenmeyi kaydet
    ProductView.objects.create(
        product    = product,
        user       = request.user if request.user.is_authenticated else None,
        ip_address = request.META.get('REMOTE_ADDR'),
    )

    base_price = float(product.discounted_price() if product.is_on_sale() else product.price)
    converted  = {
        'eur': round(base_price * rates['EUR'], 2),
        'gbp': round(base_price * rates['GBP'], 2),
        'try': round(base_price * rates['TRY'], 2),
    }

    return render(request, 'products/product_detail.html', {
        'product':   product,
        'reviews':   reviews,
        'rates':     rates,
        'converted': converted,
    })


def campaign_list(request):
    """
    Lists all active campaigns.
    """
    campaigns = Campaign.objects.filter(is_active=True)
    return render(request, 'products/campaign_list.html', {
        'campaigns': campaigns,
    })

def campaign_detail(request, pk):
    """
    Kampanyayı ve ona bağlı ürünleri çeker, indirimli fiyatları arka planda hesaplar.
    """
    # Aktif olan kampanyayı ID (pk) ile bulur, yoksa 404 verir
    campaign = get_object_or_404(Campaign, pk=pk, is_active=True)
    
    # Kampanyaya bağlı ve aktif olan ürünleri çeker
    products = campaign.products.filter(is_active=True)
    
    # Eğer views'a ürün gelmediyse, fallback (yedek) ilişkiden zorla çekmeyi dener
    if not products.exists():
        products = campaign.product_set.filter(is_active=True)
        
    # HER ÜRÜN İÇİN İNDİRİMLİ FİYATI BURADA BASİTÇE HESAPLIYORUZ
    for product in products:
        if campaign.discount:
            # Örn: 100$ fiyat ve %20 indirim -> indirim_miktari = 20$
            discount_amount = (product.price * campaign.discount) / 100
            # Net Fiyat = 100 - 20 = 80$ (Kuruş uyuşmazlığı olmasın diye 2 basamağa yuvarlıyoruz)
            product.discounted_price = round(product.price - discount_amount, 2)
        else:
            # Eğer kampanya indirimi 0 ise indirimli fiyat normal fiyata eşittir
            product.discounted_price = product.price

    return render(request, 'products/campaign_detail.html', {
        'campaign': campaign,
        'products': products,
    })
