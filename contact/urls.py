from django.urls import path
from .views import EmailView, homepage, faq
urlpatterns = [
    path('kontakt/', EmailView.as_view(), name='contact'),
    path('', homepage, name='homepage'),
    path('faq/',faq, name='faq'),
    ]