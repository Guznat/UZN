from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime
import random
import string
from accounts.models import Profile
from products.models import Product
from shopping_cart.models import OrderItem, Order


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for i in range(3)])
    return date_str + rand_str


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)

    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    if product in request.user.profile.product.all():
        messages.info(request, 'Ten produkt jest już w koszyku')
        return redirect(reverse('product_list'))
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
        product.is_available = False
        product.save()

    messages.info(request, "Dodano przedmiot do koszyka")
    return redirect(reverse('product_list'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Usunięto przedmiot z koszyka.")
    return redirect(reverse('order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    ctx = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', ctx)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    ctx = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/checkout.html', ctx)


@login_required()
def success(request):
    # profile = get_object_or_404(Profile, user=request.user)
    # order_ref = get_object_or_404(Order, owner=profile)
    order_to_purchase = get_user_pending_order(request)
    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.now()
    order_to_purchase.save()
    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered=True, date_ordered=datetime.now())
    user_profile = get_object_or_404(Profile, user=request.user)
    order_products = [item.product for item in order_items]
    user_profile.product.add(*order_products)
    user_profile.save()

    messages.info(request, "Dziękujemy, przedmiot został kupiony.")

    ctx = {
        'order': order_products,
    }
    return render(request, 'shopping_cart/purchase_success.html', ctx)
