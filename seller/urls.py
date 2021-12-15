from rest_framework import routers, urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('products', views.seller_track_pack),
    path('client', views.seller_get_clientinfo),
    path('updates', views.seller_check_updates)
]