from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import userForm

# Create your views here.


def index(request):
    return render(request, 'wfdApp/index.html')


def login(request):
    form = userForm()
    context = {'form': form}

    # when the user logs in
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'wfdApp/login.html', context)


def items(request):
    itemlist = Item.objects.all()
    return render(request, 'wfdApp/items.html', {'itemlist': itemlist})


def searcheditem(request):
    return render(request, 'wfdApp/searched_item.html')
