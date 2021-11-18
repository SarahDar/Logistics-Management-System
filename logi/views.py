from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

class SellerProductView(APIView):
	
	serializer_class = SellerProductSerializer

	def get(self, request):
		detail = [ {'sellerID':detail.sellerID, 'productID':detail.productID, 'weightPrice':detail.weightPrice, 'deliveryPrice':detail.deliveryPrice, 'sellerPrice':detail.sellerPrice}
		for detail in SellerProduct.objects.all()]
		return Response(detail)

	def post(self, request):

		serializer = SellerProductSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
