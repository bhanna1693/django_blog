from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # config stuff
    class Meta:
        model = User  # indicates that the action will affect the User
        fields = ['username', 'email', 'password1', 'password2']
