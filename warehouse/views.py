from django.shortcuts import redirect, render
from django.db import connection

# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]
    
def home(request):
    return render(request, 'WarehouseMenu.html')

def login(request):
    if request.method=='POST':
        username = request.POST['ID']
        password = request.POST['pass']
        # return redirect("/warehouse/home")
        logged_in = authenticate(username, password)
        if logged_in:
            return redirect("/warehouse/home")
        else:
            messages.info(request, "invalid credentials")
            
    else:
        return render(request, 'WarehouseLogin.html')
    
def inventory(request):
    return render(request, 'WarehouseInventory.html')

def ship_products(request):
    return render(request, 'WarehouseShipProducts.html')

def deliver_products(request):
    return render(request, 'WarehouseDeliverProducts.html')
    
def authenticate(username, password):
    with connection.cursor() as cursor:
        query = "SELECT userPassword WHERE userName=%s" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    print(rows)
    row = rows[0]
    if row["password"] == password:
        return True
    else:
        return False
    
def display_inventory(request):
    with connection.cursor() as cursor:
        # query goes here as string
        query = "SELECT * FROM Product WHERE warehouseID=Fatima"
        cursor.execute(query)
        rows = dictfetchall(cursor)