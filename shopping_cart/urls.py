from django.conf.urls import url

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    success,
    checkout
)

urlpatterns = [
    url(r'^dodaj-do-koszyka/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^koszyk/$', order_details, name="order_summary"),
    url(r'^sukces/$', success, name='purchase_success'),
    url(r'^potwierdzenie-zamowienia/$', checkout, name='checkout'),
    url(r'^przedmioty/usun/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),

]