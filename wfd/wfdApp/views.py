from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item, Request
from .forms import userForm, itemForm, requestForm, itemEditForm
# Create your views here.


def index(request):
    return render(request, 'wfdApp/index.html')


def login(request):
    form = userForm()
    context = {'form': form}

    # when the user logs in
    if request.method == 'POST':
        form = userForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password1")
        if form.is_valid():
            form.save()
            if User is None:
                user = User.objects.create(
                    username=username, password=password)
                user.save()
                login(request, user)
                HttpResponseRedirect(reverse("item"))
            else:
                login(request, user)
                HttpResponseRedirect(reverse("item"))

    return render(request, 'wfdApp/login.html', context)


def requests(request):
    requests = Request.objects.all()
    return render(request, 'wfdApp/requests.html', {'requests': requests})


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


def createRequest(request):
    form = requestForm()
    context = {'form': form}

    if request.method == 'POST':
        newRequestDate = request.POST.get('RequestDate')
        newStock = request.POST.get('Stock')
        newreqType = request.POST.get('reqType')
        newComments = request.POST.get('Comments')

        req = Request()
        req.itemName = request.POST.get('ItemName')
        req.Stock = newStock
        req.reqType = newreqType
        req.RequestDate = newRequestDate
        req.Comments = newComments

        # save
        req.save()

        # return to request screen
        return HttpResponseRedirect(reverse("requests"))

    return render(request, 'wfdApp/createRequest.html', context)


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


def editItem(request, pk):
    qSet = Item.objects.get(pk=id)
    form = itemEditForm(instance=qSet)
    if request.method == 'POST':
        form = itemEditForm(request.POST, instance=qSet)
        if form.is_valid():
            form.save()
    return render(request, 'wfdApp/editItem.html', {'form': form})


def requestDetails(request, id):
    selectedRequest = get_object_or_404(Request, pk=id)
    return render(request, 'wfdApp/itemDetails.html', {'selectedRequest': selectedRequest})


def itemDetails(request, id):
    selectedItem = get_object_or_404(Item, pk=id)
    return render(request, 'wfdApp/itemDetails.html', {'selectedItem': selectedItem})
