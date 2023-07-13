from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Account


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    country = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    btc_address = forms.CharField(max_length=500, required=True)
    etherum_address = forms.CharField(max_length=500, required=True)
    profile_picture = forms.ImageField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'phone_number', 'btc_address', 'etherum_address', 'profile_picture', 'password1', 'password2']
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username or Email')
    password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput)