import mysql.connector
import hashlib


mydb = mysql.connector.connect(user="DBproj", password="Ahsan@13", host="lms.mysql.database.azure.com", port=3306, database="logi_database", ssl_disabled=True)


# mydb = mysql.connector.connect(user="uncvgbo5tmuqtrik", password="1UkhxmRwTbYwiW7zzAjW", host="buoukgi7ixbf6uamrzmy-mysql.services.clever-cloud.com", port=3306, database="buoukgi7ixbf6uamrzmy", ssl_disabled=True)

conn_cursor = mydb.cursor()
print("STARTING")
# filling the loginInfo table with login info of all the users
# sellers deets
for user_num in range(1, 201, 1):
    username = "seller" + str(user_num)
    temp_password = "passofseller" + str(user_num)
    password = hashlib.sha256(temp_password.encode()).hexdigest()
    query = "INSERT INTO LoginInfo(ID, userName, userPassword) VALUES (%s, %s, %s);"
    try:
        conn_cursor.execute(query, ("Seller", username, password))
    except:
        pass

# warehouse deets
for user_num in range(1, 51, 1):
    username = "warehouse" + str(user_num)
    temp_password = "passofwarehouse" + str(user_num)
    password = hashlib.sha256(temp_password.encode()).hexdigest()
    query = "INSERT INTO LoginInfo(ID, userName, userPassword) VALUES (%s, %s, %s);"
    try:
        conn_cursor.execute(query, ("Warehouse", username, password))
    except:
        pass


# rider deets
for user_num in range(1, 501, 1):
    username = "rider" + str(user_num)
    temp_password = "passofrider" + str(user_num)
    password = hashlib.sha256(temp_password.encode()).hexdigest()
    query = "INSERT INTO LoginInfo(ID, userName, userPassword) VALUES (%s, %s, %s);"
    try:
        conn_cursor.execute(query, ("Rider", username, password))
    except:
        pass

print("LOGINS DONE")

# client table creation
client_numbers = []
cities = ['Lahore', 'Karachi', 'gwadar', 'Islamabad', 'Rawalpindi', 'Sialkot', 'Faisalabad', 'Quetta']
for num in range(1, 1001, 1):
    number = 923001111111 + num;
    client_numbers.append(number)
    addr = "address of client " + str(num)
    city = cities[num % 8]
    query = "INSERT INTO Client(phoneNumber, clientAddress, city) VALUES (%s, %s, %s);"
    # try:
    conn_cursor.execute(query, (str(number), addr, city))
    #     print("error")
    # except:
    #     pass


# seller table creation
cities = ['Lahore', 'Karachi', 'gwadar', 'Islamabad', 'Rawalpindi', 'Sialkot', 'Faisalabad', 'Quetta']
for num in range(1, 201, 1):
    ID = "seller" + str(num)
    name = "nameSeller" + str(num)
    number = 923001111111 + num;
    # addr = "address of client " + str(num)
    city = cities[num % 8]
    query = "INSERT INTO Seller(sellerID, sellerName, phoneNumber, city) VALUES (%s, %s, %s, %s);"
    # try:
    conn_cursor.execute(query, (str(ID), name, str(number),city))
    # except:
    #     pass


# warehouse table creation
cities = ['Lahore', 'Karachi', 'gwadar', 'Islamabad', 'Rawalpindi', 'Sialkot', 'Faisalabad', 'Quetta', 'hyderabad', 'sukkhur', 'mianwali', 'chiniot', 'naran', 'kaghan', 'murree', 'new york', 'london', 'bristol', 'cambridge', 'boston', 'miami', 'LA', 'providence', 'morocco', 'Adoni', 'Amaravati', 'Chandragiri', 'Chittoor', 'Dowlaiswaram', 'Rajahmundry', 'Srikakulam', 'Tirupati', 'Chapra', 'Pusa', 'Saharsa', 'Bharuch', 'Godhra', 'Palanpur', 'Faridabad', 'Hisar', 'Panipat', 'Dalhousie', 'Kullu', 'Anantnag', 'Srinagar', 'Deoghar', 'Jharia', 'Ranchi', 'Bengaluru', 'Bhadravati', 'boriwalii', 'somecity']
for num in range(1, 51, 1):
    ID = "warehouse" + str(num)
    city = cities[num]
    query = "INSERT INTO Warehouse(warehouseID, city) VALUES (%s, %s);"
    # try:
    conn_cursor.execute(query, (str(ID), city))
    # except:
    #     pass

print("waredone")


locations = ['karakoram HW', 'GT road', 'shahra e faisal', 'motorway', 'national HW', 'Mall road', 'MM Alam', 'D ground', 'D chowk', 'gwadar port', 'china border', 'India border', 'afghan border', 'balochistan road', 'shalimar', 'hall road', 'hafeez center']
prices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 500]
# creating products table
client_num = 0
track_num = 10000
ware_num = 1
for num in range(1, 201, 1): #sellers
    for product in range(1, 51, 1): # each selling
        trackingID = track_num
        sellerID = "seller" + str(num)
        warehouseID = "warehouse" + str(ware_num)
        if ware_num % 200 == 0:
            ware_num += 1
        track_num += 1
        loc = locations[(product * num) % 17]
        route = "route" + str(product//2 + 1)
        if product % 2 == 0:
            pay = 1
        else:
            pay = 0
        price = prices[(num * product) % 20]
        number = client_numbers[client_num]
        client_num += 1
        if client_num > 999:
            client_num = 0
        query = "INSERT INTO Product(trackingID, sellerID, warehouseID, currentLocation, productRoute, paymentStatus, price, clientPhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        # try:
        conn_cursor.execute(query, (str(trackingID), str(sellerID), str(warehouseID), loc, route, pay, price, str(number)))
        # except:
        #     pass
        
print("products done")
# creating entries for rider table creation
counter = 1
for warehouse in range(1, 51, 1):
    for rider in range(1, 11, 1):
        for item in range(1, 21, 1):
            riderID = "rider" + str(counter)
            riderName = "ridername" + str(counter)
            num = 563222222222 + counter
            warehouseID = "warehouseID" + str(warehouse)
            prodID = 10000 + counter
            counter += 1 
            query = "INSERT INTO Rider(riderID, riderName, phoneNumber, warehouseID, productID) VALUES (%s, %s, %s, %s, %s);"
            # try:
            conn_cursor.execute(query, (str(riderID), str(riderName), str(num), warehouseID, prodID))
            # except:
            #     pass




mydb.commit()


query = "select * from LoginInfo"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))


query = "select * from Client"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))

query = "select * from Seller"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))

query = "select * from Warehouse"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))

query = "select * from Rider"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))

query = "select * from Product"
conn_cursor.execute(query)
print(len(conn_cursor.fetchall()))