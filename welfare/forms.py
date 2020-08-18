from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistration(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['first name', 'last name', 'username', 'email', 'password']
