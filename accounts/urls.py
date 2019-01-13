from django.urls import path
from .views import AddUserView, UserDetailView, change_password, UserOrderView, UpdateUserProfile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('rejestracja/', AddUserView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profil/<int:id>', UserDetailView.as_view(), name='my_profile'),
    path('zmiana_hasla/', change_password, name='change_password'),
    path('zmiana_danych/', UpdateUserProfile.as_view(), name='profile_update'),
    path('profil/<int:id>/zamowienia', UserOrderView.as_view(), name='user_orders'),
]
