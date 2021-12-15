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
    return render(request, 'SellerMenu.html')

def home_wargs(request, username):
    # for testing purposes, we are returning obtain seller related product information
    with connection.cursor() as cursor:
        query = "SELECT * FROM Seller WHERE sellerID=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)

    return render(request, 'SellerTrackPackages.html', {'data': rows})


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        logged_in = authenticate(username, password)
        if logged_in:
            print("authentication was successful")
            return redirect('/seller/home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/')

    else:
        return render(request, 'SellerLogin.html')

def seller_track_pack(request):
    return render(request, 'SellerTrackProductDets.html')

def seller_get_clientinfo(request):
    return render(request, 'SellerObtainClientInfo.html')

def seller_check_updates(request):
    return render(request, 'SellerCheckUpdates.html')

def authenticate(username, password):
    if username == "":
        return False

    with connection.cursor() as cursor:
        query = "SELECT userPassword FROM LoginInfo WHERE LoginInfo.ID=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)
    
    if rows is not None:
        print(rows)
        row = rows[0]
        if row["userPassword"] == password:
            return True
        else:
            return False
    else:
        return False