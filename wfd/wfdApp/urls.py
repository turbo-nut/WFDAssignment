from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("items/", views.items, name="item"),
    path("search/", views.searcheditem, name="search"),
    path("createItem/", views.createItem, name="createItem"),
    path("itemDetails/<id>", views.itemDetails, name='itemDetails'),
]
