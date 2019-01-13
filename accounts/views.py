from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.models import User
from .forms import CreateUserForm, UpdateUserForm
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from shopping_cart.models import Order
from .models import Profile



class AddUserView(View):
    def get(self, request):
        form = CreateUserForm()
        ctx = {
            'form': form
        }
        return render(request, 'registration/signup.html', ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            login(request, user)
            return redirect(reverse('product_list'))
        return render(request, 'registration/signup.html', ctx)


class UpdateUserProfile(View, LoginRequiredMixin):
    def get(self, request):
        form = UpdateUserForm()
        ctx = {
            'form': form
        }
        return render(request, 'accounts/profile_update.html', ctx)

    def post(self, request):
        form = UpdateUserForm(request.POST or None, request.FILES or None)
        ctx = {
            'form': form
        }
        if form.is_valid():
            User.objects.update(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return redirect(reverse('product_list'))
        return render(request, 'accounts/profile_update.html', ctx)

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Udało się, hasło zostało zmienione!')
            return redirect('homepage')
        else:
            messages.error(request, 'Proszę poprawić błąd.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


class UserDetailView(View, LoginRequiredMixin):
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        fav = Product.objects.filter(favourite=user.id)
        my_user_profile = Profile.objects.filter(user=request.user).first()
        my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)

        ctx = {
            'user': user,
            'fav': fav,
            'my_orders': my_orders
        }
        return render(request, 'accounts/profile_detail.html', ctx)


class UserOrderView(View, LoginRequiredMixin):
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        my_user_profile = Profile.objects.filter(user=request.user).first()
        my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
        ctx = {
            'my_orders': my_orders,
            'user': user
        }
        return render(request, 'accounts/user_orders.html', ctx)
