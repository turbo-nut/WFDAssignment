# using a separate python file for form creation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item


class userForm(UserCreationForm):
    class Login:
        model = User
        # fields will have a username + password
        fields = ['username', 'password1']


class itemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["ItemName", "Category", "Stock", "RetailPrice"]
