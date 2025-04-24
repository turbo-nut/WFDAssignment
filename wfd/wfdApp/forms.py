# using a separate python file for form creation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item, Request


class dateInput(forms.DateInput):
    input_type = 'date'


class requestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["ItemName", "RequestDate", "NewStock", "reqType", "Comments"]
        widgets = {
            'RequestDate': dateInput(),
        }


class userForm(UserCreationForm):
    class Login:
        model = User
        # fields will have a username + password
        fields = ['username', 'password1']


class itemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["ItemName", "Category", "Stock", "RetailPrice"]


class itemEditForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["ItemName", "Category", "Stock", "RetailPrice"]
