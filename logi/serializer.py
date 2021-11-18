from rest_framework import serializers
from . models import *


class SellerProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = SellerProduct
		fields = ['sellerID', 'productID', 'weightPrice', 'deliveryPrice', 'sellerPrice']
