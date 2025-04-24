from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Item
from .forms import userForm, itemForm
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
    query = request.GET.get('q')
    if query:
        results = Item.objects.filter(name__icontains=query)
    else:
        results = Item.objects.none()
    return render(request, 'wfdApp/search.html', {'results': results})


def createItem(request):
    form = itemForm()
    context = {'form': form}

    if request.method == 'POST':
        newItemID = request.POST.get('ItemID')
        newItemStock = request.POST.get('Stock')
        newItemCategory = request.POST.get('Category')
        newItemName = request.POST.get('ItemName')
        newItemPrice = request.POST.get('RetailPrice')

        item = Item()
        item.ItemID = newItemID
        item.Stock = newItemStock
        item.Category = newItemCategory
        item.ItemName = newItemName
        item.RetailPrice = newItemPrice

        # save
        item.save()

        # make it so that when the item is saved the user sees the webpage of that item
        return HttpResponseRedirect(reverse("itemDetails", kwargs={'id': item.pk}))

    return render(request, 'wfdApp/createItem.html', context)


def itemDetails(request, id):
    return render(request, 'wfdApp/itemDetails.html', {})
