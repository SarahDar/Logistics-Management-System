from django.db import models

# Create your models here.

# Relation Classes

class SellerProduct(models.Model):
    sellerID= models.CharField(max_length=10)
    productID= models.CharField(max_length=10)
    weightPrice= models.DecimalField(max_digits=10, decimal_places=2)
    deliveryPrice = models.DecimalField(max_digits=10, decimal_places=2)
    sellerPrice = models.DecimalField(max_digits=10, decimal_places=2)
    
class ClientProduct(models.Model):
    clientPhoneNumber = models.IntegerField()
    productID= models.CharField(max_length=10)
    deliveryAddress = models.CharField(max_length=70)

class Login(models.Model):
    ID = models.CharField(max_length=10)
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

# Entity Classes 

class Client(models.Model):
    phoneNumber = models.IntegerField()
    localAddress = models.CharField(max_length=70)
    city = models.CharField(max_length=15)

class Seller(models.Model):
    sellerID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    phoneNumber = models.IntegerField()
    city = models.CharField(max_length=15)
    
class Warehouse(models.Model):
    warehouseID = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    
class Product(models.Model):
    trackingID = models.CharField(max_length=10)
    sellerID = models.CharField(max_length=10)
    warehouseID = models.CharField(max_length=10)
    location = models.CharField(max_length=15)
    route = models.CharField(max_length=30)
    paymentStatus = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    clientPhoneNumber = models.IntegerField()
    
class Rider(models.Model):
    riderID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    warehouseID = models.CharField(max_length=10)
    productID = models.CharField(max_length=10)

