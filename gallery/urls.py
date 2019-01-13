from django.conf.urls import url
from django.urls import path

from .views import TopicListView, GalleryDetailView, GalleryListView

urlpatterns = [
    path('galeria/',TopicListView.as_view(), name='index'),
    path('galeria/<int:id>/', GalleryListView.as_view(), name='topic'),
    url(r'^galeria/media/(?P<pk>[0-9]+)/$', GalleryDetailView.as_view(), name='detail')
]



#TODO galeria/id-topicu/id-zdjecia, tymczasowe
# rozwiązanie to przekierowaie od razu do id zdjecia przez /media/