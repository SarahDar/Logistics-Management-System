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

def home_wargs(request, id):
    # for testing purposes, we are returning obtain seller related product information
    with connection.cursor() as cursor:
        query = "SELECT * FROM Seller WHERE sellerID=\"%s\";" % id
        cursor.execute(query)
        rows = dictfetchall(cursor)

    return render(request, 'SellerMenu.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # username = 'sellerID'

        logged_in = authenticate(username, password)

        if logged_in:
            id = get_id(username)
            request.session["ID"] = id
            return home_wargs(request, id)
        else:
            messages.info(request, "invalid credentials")
            return redirect('/seller') # add 

    else:
        return render(request, 'SellerLogin.html')

# seller track specific package
def seller_track_pack(request):
    if request.method=='POST':
        product_id = request.POST['productid']
        return seller_track_pack_res(request, product_id)
    else:    
        return render(request, 'SellerTrackProductDets.html')

def seller_track_pack_res(request, prod_id):
    with connection.cursor() as cursor:
        query = "SELECT *  FROM Product WHERE trackingID=\"%s\";" % prod_id
        cursor.execute(query)
        rows = dictfetchall(cursor)

    # only one row so we index and get first
    row = rows[0]
    return render(request, "SellerTrackProductDetsResultz.html", {'data': row})

# seller get client information
def seller_get_clientinfo(request):
    return render(request, 'SellerObtainClientInfo.html')


# seller check for updates
def seller_check_updates(request):
    session_id = request.session["ID"]

    with connection.cursor() as cursor:
        query = "SELECT trackingID, warehouseID, currentLocation, productRoute, paymentStatus, price FROM Product WHERE sellerID = \"%s\";" % session_id
        cursor.execute(query)
        rows = dictfetchall(cursor)

    return render(request, 'SellerCheckUpdates.html', {'data': rows})

#### HELPER FUNCTIONS

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
