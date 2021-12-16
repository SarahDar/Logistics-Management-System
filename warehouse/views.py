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


def home(request):
    # for testing purposes, we are returning obtain seller related product information
    # with connection.cursor() as cursor:
    #     query = "SELECT * FROM Warehouse WHERE warehouseID=\"%s\";" % id
    #     cursor.execute(query)
    #     rows = dictfetchall(cursor)
    return render(request, 'WarehouseMenu.html')

def login(request):
    if request.method=='POST':
        username = request.POST['city']
        password = request.POST['password']

        logged_in = authenticate(username, password)

        if logged_in:
            id = get_id(username)
            request.session["ID"] = id
            return home(request)
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
        query = "SELECT * FROM Product WHERE currentLocation=\"%s\";" % request.session["ID"]
        cursor.execute(query)
        rows = dictfetchall(cursor)
    return render(request, 'WarehouseInventory.html', {'data': rows})


def ship_products(request):
    if request.method=='POST':
        product = request.POST['id']
        dest = request.POST['warehouse']

        id = request.session["ID"]
        ship = product_exists(product, id)
        ship = warehouse_exists(dest)

        if ship:
            with connection.cursor() as cursor:
                q1 = "SELECT warehouseID FROM Warehouse WHERE Warehouse.city = \"%s\";"%dest
                cursor.execute(q1)
                rows = dictfetchall(cursor)
                if not rows:
                    row = None
                else:
                    row = rows[0]
                dest_id = row["warehouseID"]
                shift_product = "UPDATE Product SET Product.warehouseID = \"{}\",Product.currentlocation = \"{}\" WHERE Product.warehouseID=\"{}\";".format(dest_id,dest_id,id)
                cursor.execute(shift_product)
            return render(request, 'WarehouseShipped.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/warehouse/ship')  
    else:
        with connection.cursor() as cursor:
        # query goes here as string
            query = "SELECT Product.trackingID FROM Product WHERE currentLocation=\"%s\";" % request.session["ID"]
            cursor.execute(query)
            rows = dictfetchall(cursor)
        return render(request, 'WarehouseShipProducts.html', {'data': rows})

def warehouse_exists(dest):
    if dest == "":
        return False

    with connection.cursor() as cursor:
        query = "SELECT city FROM Warehouse WHERE Warehouse.city=\"%s\";" % dest
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    if rows is not None:
        print("rows exist")
        for row in rows:
            if row["city"] == dest:
                return True
            else:
                return False
        return False
    else:
        return False

def product_exists(product, id):
    if product == "":
        return False

    with connection.cursor() as cursor:
        print(id)
        query = "SELECT trackingID FROM Product WHERE Product.warehouseID=\"%s\";" % id
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    if rows is not None:
        print("rows exist")
        for row in rows:
            if row["trackingID"] == product:
                return True
            else:
                return False
        return False
    else:
        return False


def deliver_products(request):
    return render(request, 'WarehouseDeliverProducts.html')
    
