# using a separate python file for form creation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class userForm(UserCreationForm):
    class Login:
        model = User
        # fields will have a username + password
        fields = ['username', 'password1']
