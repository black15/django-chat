from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Account

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UpdateUserInfo(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'profile_img', 'bio', 'hide_email']