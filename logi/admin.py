from django.contrib import admin

# Register your models here.
from .models import SellerProduct
from .models import ClientProduct
from .models import Login

from .models import Seller
from .models import Client
from .models import Warehouse
from .models import Product
from .models import Rider
    
admin.site.register(SellerProduct)
admin.site.register(ClientProduct)
admin.site.register(Login)

admin.site.register(Seller)
admin.site.register(Client)
admin.site.register(Warehouse)
admin.site.register(Rider)
admin.site.register(Product) 