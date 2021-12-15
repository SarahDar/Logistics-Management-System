from django.shortcuts import render
from django.db import connection

# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def home(request):
    return render(request, 'SellerMenu.html')

def seller_track_pack(request):
    return render(request, 'SellerTrackProductDets.html')

def seller_get_clientinfo(request):
    return render(request, 'SellerObtainClientInfo.html')

def seller_check_updates(request):
    return render(request, 'SellerCheckUpdates.html')