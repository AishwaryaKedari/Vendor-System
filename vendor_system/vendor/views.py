# from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from vendor.models import Purchase_Orders
from vendor.serializers import Purchase_OrdersSerializer
# from .models import *

# Create your views here.
# class VendorViewSet(viewsets.ModelViewSet):
#     queryset=Vendors.objects.all()
#     serializer_class = VendorSerializer

class Purchase_OrdersView(APIView):
    def post(self,request,format=None):
        serializer= Purchase_OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"List Of Purchase Orders",'status':'success','candidate':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def get(self,request,format=None):
        Orders = Purchase_Orders.objects.all()
        serializer = Purchase_OrdersSerializer(Orders,many=True)
        return Response({'status':'sucess','Orders':'serializer'.data},status=status.HTTP_200_OK)


# def update_items(acknowledgment_date, pk):
#     Purchase_Orders = Purchase_Orders.objects.all()
#     data = Purchase_OrdersSerializer(instance=Purchase_Orders, data=acknowledgment_date.data)
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)