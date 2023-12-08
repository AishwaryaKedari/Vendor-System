from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from vendor.models import Vendors,Purchase_Orders
from vendor.serializers import VendorSerializer,Purchase_OrdersSerializer

# Create your views here.
class VendorViewSet(viewsets.ModelViewSet):
    queryset=Vendors.objects.all()
    serializer_class = VendorSerializer

class Purchase_OrdersViewSet(viewsets.ModelViewSet):
    queryset= Purchase_Orders.objects.all()
    serializer_class = Purchase_OrdersSerializer