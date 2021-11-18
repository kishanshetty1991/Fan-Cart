from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "ShopHome"),
    path('about/', views.about, name= "About"),
    path('contact/', views.contact, name= "Contact"),
    path('tracker/', views.tracker, name= "Tracker"),
    path('products/<int:myid>', views.product, name= "Product_View"),
    path('search/', views.search, name= "Search"),
    path('checkout/', views.checkout, name= "Checkout"),

]