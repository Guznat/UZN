from django.urls import path
from django.conf.urls import url
from .views import ProductListView, ProductDetailView, PictureImageDetailView, favourite_product
urlpatterns = [
    path('produkty/', ProductListView.as_view(), name='product_list'),
    # url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    path('produkty/<int:id>', ProductDetailView.as_view(), name='product_detail'),
    url(r'^produkty/media/(?P<pk>[0-9]+)/$', PictureImageDetailView.as_view(), name='product_detail_picture'),
    path('ulubione/', favourite_product, name='favourite_product')
    ]