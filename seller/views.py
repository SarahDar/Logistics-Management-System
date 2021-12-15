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
    return render(request, 'SellerMenu.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
    
        logged_in = authenticate(username, password)
        if logged_in:
            return redirect("home")
        else:
            messages.info(request, "invalid credentials")

    else:
        return render(request, 'SellerLogin.html')

def seller_track_pack(request):
    return render(request, 'SellerTrackProductDets.html')

def seller_get_clientinfo(request):
    return render(request, 'SellerObtainClientInfo.html')

def seller_check_updates(request):
    return render(request, 'SellerCheckUpdates.html')

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