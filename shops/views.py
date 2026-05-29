from django.shortcuts import render
from .models import Shop

def shop_list(request):
    shops = Shop.objects.filter(is_active=True)
    return render(request, 'shops/shop_list.html', {'shops': shops})
