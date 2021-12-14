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