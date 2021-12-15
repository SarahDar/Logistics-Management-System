from django.shortcuts import redirect, render
from django.db import connection
from django.contrib import messages

# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def home(request, id):
    # for testing purposes, we are returning obtain seller related product information
    with connection.cursor() as cursor:
        query = "SELECT * FROM Warehouse WHERE warehouseID=\"%s\";" % id
        cursor.execute(query)
        rows = dictfetchall(cursor)
    return render(request, 'WarehouseMenu.html')

def login(request):
    if request.method=='POST':
        username = request.POST['city']
        password = request.POST['password']

        logged_in = authenticate(username, password)

        if logged_in:
            id = get_id(username)
            request.session["ID"] = id
            return home(request, id)
        else:
            messages.info(request, "invalid credentials")
            return redirect('/warehouse')  

    else:
        return render(request, 'WarehouseLogin.html')
    
def authenticate(username, password):
    if username == "":
        return False

    with connection.cursor() as cursor:
        query = "SELECT userPassword FROM LoginInfo WHERE LoginInfo.userName=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    if rows is not None:
        for row in rows:
            if row["userPassword"] == password:
                return True
            else:
                return False
        return False
    else:
        return False

def get_id(username):
    with connection.cursor() as cursor:
        query = "SELECT ID FROM LoginInfo WHERE LoginInfo.userName=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)

    id = rows[0]
    return id["ID"]
    
def inventory(request):
    with connection.cursor() as cursor:
        # query goes here as string
        query = "SELECT * FROM Product WHERE warehouseID=\"%s\";" % request.session["ID"]
        cursor.execute(query)
        rows = dictfetchall(cursor)
    return render(request, 'WarehouseInventory.html', {'data': rows})

def ship_products(request):
    return render(request, 'WarehouseShipProducts.html')

def deliver_products(request):
    return render(request, 'WarehouseDeliverProducts.html')
    
def authenticate(username, password):
    with connection.cursor() as cursor:
        query = "SELECT userPassword FROM LoginInfo WHERE userName=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    if rows is not None:
        for row in rows:
            if row["userPassword"] == password:
                return True
            else:
                return False
        return False
    else:
        return False
    