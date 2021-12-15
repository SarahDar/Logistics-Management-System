from rest_framework import routers, urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('home', views.home),
    path('deliver', views.deliver_products),
    path('ship', views.ship_products),
    path('inventory', views.inventory)
]