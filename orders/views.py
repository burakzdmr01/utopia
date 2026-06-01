from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from products.models import Product
from django.http import JsonResponse

@login_required
def add_to_cart_ajax(request, product_id):
    """AJAX endpoint for adding a product to cart. Returns JSON response."""
    if request.method == 'POST':
        product      = get_object_or_404(Product, id=product_id)
        cart, _      = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        cart_count = cart.items.count()
        return JsonResponse({
            'success': True,
            'cart_count': cart_count,
            'message': f'{product.name} added to cart!'
        })
    return JsonResponse({'success': False}, status=400)

@login_required
def cart_view(request):
	    """Displays the current user's shopping cart."""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'orders/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
	    """Adds a product to the cart or increments quantity if already present."""
    product  = get_object_or_404(Product, id=product_id)
    cart, _  = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('orders:cart')

@login_required
def remove_from_cart(request, item_id):
	    """Removes a specific item from the cart."""
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('orders:cart')

@login_required
def checkout_view(request):
	    """Handles checkout process and creates an order from cart items."""
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            shipping_address=request.POST.get('address'),
            total_price=cart.get_total(),
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        cart.items.all().delete()
        return redirect('orders:order_list')
    return render(request, 'orders/checkout.html', {'cart': cart})

@login_required
def order_list(request):
	    """Lists all orders for the currently logged-in user."""
    orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
