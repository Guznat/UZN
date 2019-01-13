from django.shortcuts import render, redirect
from .models import Product, ExtraProductPicture, Category
from django.views.generic import ListView, DetailView
from django.views import View
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from shopping_cart.models import Order




class ProductListView(ListView):
    template_name = "products/product_list.html"
    context_object_name = 'object_list'
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__contains=query)
                )

        return qs.order_by("-add_date")

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({
            'category': Category.objects.order_by('name'),
        })
        return context


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        extra_pictures = ExtraProductPicture.objects.filter(product_id=id)
        if request.user.is_anonymous:
            ctx = {
                'product': product,
                'extra_pictures': extra_pictures}
            return render(request, 'products/product_detail.html', ctx)

        is_favourited = False

        if product.favourite.filter(id=request.user.id).exists():
            is_favourited = True

        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []

        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]
        ctx = {
            'product': product,
            'extra_pictures': extra_pictures,
            'is_favourited': is_favourited,
            'total_fav': product.total_fav(),
            'current_order_products': current_order_products
        }
        return render(request, 'products/product_detail.html', ctx)

def favourite_product(request):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    is_favourited = False
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        is_favourited = False

    else:
        product.favourite.add(request.user)
        is_favourited = True


    return HttpResponseRedirect(product.get_absolute_url())

class PictureImageDetailView(DetailView):
    queryset = ExtraProductPicture.objects.all()
    template_name = 'products/product_detail_picture.html'

#TODO wydaje mi sie ze przy duzej ilosci zdj opcja .all() bedzie nieoptymalna





