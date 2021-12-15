from django.shortcuts import render
from django.db import connection

# Create your views here.

def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def client_home(request):
    return render(request, 'ClientMenu.html')

def client_track_pack(request): 
    return render(request, 'ClientTrackPackages.html')

def client_seller_info(request): #TODO: take input
    return render(request, 'ClientObtainSellerInfo.html')

def client_prod_details(request): #TODO: take input
    return render(request, 'ClientTrackProductDets.html')

def client_rider_info(request): #TODO: take input
    return render(request, 'ClientTrackRiderInfo.html')

def client_currentloc(request): #TODO: take input
    return render(request, 'ClientTrackCurrentLoc.html')


def clients(request):
    with connection.cursor() as cursor:
        # query goes here as string
        query = "SELECT * FROM Client WHERE phoneNumber=032028588"
        cursor.execute(query)
        rows = dictfetchall(cursor)

    print(rows)
    return render(request, 'output.html',{'data':rows})

def products_info(request):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Client WHERE phoneNumber=032028588"
        cursor.execute(query)
        rows = dictfetchall(cursor)

    print(rows)
    return render(request, 'products_info.html', {'data':rows})