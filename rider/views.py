from django.shortcuts import render, redirect
from django.db import connection

import rider

# Create your views here.


def home(request):
    return render(request, 'RiderMenu.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password = hashlib.sha256(password.encode()).hexdigest()

        logged_in = authenticate(username, password)

        if logged_in:
            # id = get_id(username)
            request.session["ID"] = username
            return redirect('/rider/home')
        else:
            return redirect('/rider')  # add

    else:
        return render(request, 'RiderLogin.html')

# OBTAIN CLIENT INFORMATION

def get_client_information(request):
    riderID = request.session["ID"]

    with connection.cursor() as cursor:
        query = "SELECT productID FROM Rider WHERE riderID=\"{}\";".format(
            riderID)
        cursor.execute(query)
        rows = dictfetchall(cursor)
    if rows:
        row = rows[0]

        product_id = row["productID"]

        with connection.cursor() as cursor:
            query = "SELECT * FROM Product WHERE Product.trackingID=\"{}\";".format(
                product_id)
            cursor.execute(query)
            rows = dictfetchall(cursor)
        if rows:
            productData = rows[0]
        else:
            productData = None
    else:
        productData = None
    if productData:
        clientPhoneNumber = productData["clientPhoneNumber"]
        with connection.cursor() as cursor:
            query = "SELECT * FROM Client WHERE Client.phoneNumber=\"{}\";".format(
                clientPhoneNumber)
            cursor.execute(query)
            rows = dictfetchall(cursor)
        clientData = rows[0]
    else:
        clientData = None

    return render(request, "RiderObtainClientInfoResult.html", {"clientData": clientData})

    # if request.method == 'POST':
    #     # get client information using the product id
    #     if productData:
    #         clientPhoneNumber = productData["clientPhoneNumber"]
    #         with connection.cursor() as cursor:
    #             query = "SELECT * FROM Client WHERE Client.phoneNumber=\"{}\";".format(
    #                 clientPhoneNumber)
    #             cursor.execute(query)
    #             rows = dictfetchall(cursor)
    #         clientData = rows[0]
    #     else:
    #         clientData = None

    #     return render(request, "RiderObtainClientInfoResult.html", {"clientData": clientData})
    # else:
    #     return render(request, "RiderObtainClientInfo.html", {"productData": productData})


# OBTAIN SELLER INFORMATION
def get_seller_information(request):
    riderID = request.session["ID"]

    with connection.cursor() as cursor:
        query = "SELECT productID FROM Rider WHERE riderID=\"{}\";".format(
            riderID)
        cursor.execute(query)
        rows = dictfetchall(cursor)

    if rows:
        row = rows[0]

        product_id = row["productID"]

        with connection.cursor() as cursor:
            query = "SELECT * FROM Product WHERE Product.trackingID=\"{}\";".format(
                product_id)
            cursor.execute(query)
            rows = dictfetchall(cursor)
        if rows:
            productData = rows[0]
        else:
            productData = None
    else:
        productData = None

    if productData:
            sellerID = productData["sellerID"]
            with connection.cursor() as cursor:
                query = "SELECT * FROM Seller WHERE Seller.sellerID=\"{}\";".format(
                    sellerID)
                cursor.execute(query)
                rows = dictfetchall(cursor)
            sellerData = rows[0]
    else:
        sellerData = None
    return render(request, 'RiderObtainSellerInfoResult.html', {"sellerData": sellerData})

    # if request.method == 'POST':
    #     if productData:
    #         sellerID = productData["sellerID"]
    #         with connection.cursor() as cursor:
    #             query = "SELECT * FROM Seller WHERE Seller.sellerID=\"{}\";".format(
    #                 sellerID)
    #             cursor.execute(query)
    #             rows = dictfetchall(cursor)
    #         sellerData = rows[0]
    #     else:
    #         sellerData = None
    #     return render(request, 'RiderObtainSellerInfoResult.html', {"sellerData": sellerData})
    # else:
    #     return render(request, 'RiderObtainSellerInfo.html', {"productData": productData})


# ACCESS PRODUCT DETAILS
def get_product_details(request):
    riderID = request.session["ID"]

    with connection.cursor() as cursor:
        query = "SELECT productID FROM Rider WHERE riderID=\"{}\";".format(
            riderID)
        cursor.execute(query)
        rows = dictfetchall(cursor)
    if rows:
        row = rows[0]

        product_id = row["productID"]

        with connection.cursor() as cursor:
            query = "SELECT * FROM Product WHERE Product.trackingID=\"{}\";".format(
                product_id)
            cursor.execute(query)
            rows = dictfetchall(cursor)
        if rows:
            productData = rows[0]
        else:
            productData = None
    else:
        productData = None

    return render(request, 'RiderProductDets.html', {"productData": productData})


# FINANCES, using this to mark completed delivery. not keeping track of actual finances for now
def get_finances(request):
    riderID = request.session["ID"]

    with connection.cursor() as cursor:
        query = "SELECT productID FROM Rider WHERE riderID=\"{}\";".format(
            riderID)
        cursor.execute(query)
        rows = dictfetchall(cursor)
    if rows:
        row = rows[0]

        product_id = row["productID"]

        with connection.cursor() as cursor:
            query = "SELECT * FROM Product WHERE Product.trackingID=\"{}\";".format(
                product_id)
            cursor.execute(query)
            rows = dictfetchall(cursor)
        if rows:
            productData = rows[0]
        else:
            productData = None
    else:
        productData = None

    if request.method == "POST":
        productID = request.POST["productid"]

        with connection.cursor() as cursor:
            query = "SELECT * FROM Rider WHERE riderID=\"{}\" AND productID = \"{}\";".format(
                riderID, productID)
            cursor.execute(query)
            rows = dictfetchall(cursor)

        if len(rows):
            # successfully found product
            with connection.cursor() as cursor:
                query = "UPDATE Rider SET Rider.productID = NULL WHERE riderID=\"{}\"".format(
                    riderID)
                cursor.execute(query)
            with connection.cursor() as cursor:
                query = "UPDATE Product SET Product.currentLocation = \"Delivered\";"
                cursor.execute(query)

        with connection.cursor() as cursor:
            query = "SELECT productID FROM Rider WHERE riderID=\"{}\";".format(
                riderID)
            cursor.execute(query)
            rows = dictfetchall(cursor)

        if not rows:
            row = rows[0]

            product_id = row["productID"]

            with connection.cursor() as cursor:
                query = "SELECT * FROM Product WHERE Product.trackingID=\"{}\";".format(
                    product_id)
                cursor.execute(query)
                rows = dictfetchall(cursor)
            productData = rows[0]

        else:
            productData = None

        return render(request, 'RiderFinances.html', {"productData": productData})

    else:
        return render(request, 'RiderFinances.html', {"productData": productData})


# HELPER FUNCTIONS

def authenticate(username, password):
    if username == "":
        return False

    with connection.cursor() as cursor:
        # query = "SELECT userPassword FROM LoginInfo WHERE LoginInfo.userName=\"%s\";" % username
        query = "SELECT userPassword FROM LoginInfo WHERE LoginInfo.ID=\"{}\";".format(
            username)
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
        query = "SELECT ID FROM LoginInfo WHERE LoginInfo.ID=\"%s\";" % username
        cursor.execute(query)
        rows = dictfetchall(cursor)

    id = rows[0]
    return id["ID"]


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
