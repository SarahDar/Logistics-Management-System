from rest_framework import routers, urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products_info),
    path('home_view', views.clients),
    path('', views.client_home)
]
