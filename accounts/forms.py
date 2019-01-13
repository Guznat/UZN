import django.forms as forms
import django.core.validators as validators
from django.contrib.auth.models import User

class CreateUserForm(forms.Form):
    login = forms.CharField(max_length=24)
    password = forms.CharField(max_length=48, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=48, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=24)
    last_name = forms.CharField(max_length=24)
    email = forms.EmailField(max_length=24, widget=forms.EmailInput)

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('Hasło nie jest takie same.')
        if User.objects.filter(username=data['login']):
            raise forms.ValidationError('Taki użytkownik już istnieje.')
        return data

class UpdateUserForm(forms.Form):
    first_name = forms.CharField(max_length=24)
    last_name = forms.CharField(max_length=24)
    email = forms.EmailField(max_length=24, widget=forms.EmailInput)