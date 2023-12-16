# from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status,permissions
from vendor.models import Purchase_Orders
from vendor.serializers import Purchase_OrdersSerializer


# Create your views here.

# class VendorViewSet(viewsets.ModelViewSet):
#     queryset=Vendors.objects.all()
#     serializer_class = VendorSerializer

class Purchase_OrdersView(APIView):
    # permission_classes=(permissions.AllowAny)
    http_method_names=['GET','POST']
    serializer_class=Purchase_OrdersSerializer
    def GET(self,request,pk=None):
        if pk is not None:
            Purchase_Orders=Purchase_Orders.objects.get(pk=pk)
            serializer=Purchase_OrdersSerializer(Purchase_Orders)
            return Response(serializer.data)
        else:
            Purchase_Orders=Purchase_Orders.objects.all()
            serializer=Purchase_OrdersSerializer(Purchase_Orders,many=True)
            return Response(serializer.data)
        
    def POST(self,request):
        serializer=Purchase_OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def PUT(self,request,pk=None):
        if pk is not None:
            Purchase_Orders=Purchase_Orders.objects.get(pk=pk)
            serializer=Purchase_OrdersSerializer(Purchase_Orders,data=request.data)
            if serializer . is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({'error':'Please provide ID'},status=status.HTTP_400_BAD_REQUEST)

    # def POST(self,request):
    #     serializer= Purchase_OrdersSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response({"Message":"List Of Purchase Orders",'status':'success','candidate':serializer.data},status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors)


    # def GET(self,request):
    #     Orders = Purchase_Orders.objects.all()
    #     serializer = Purchase_OrdersSerializer(Orders,many=True)
    #     return Response({'status':'sucess','Orders':'serializer'.data},status=status.HTTP_200_OK)


    # def update_items(acknowledgment_date, pk):
    #     Purchase_Orders = Purchase_Orders.objects.all()
    #     data = Purchase_OrdersSerializer(instance=Purchase_Orders, data=acknowledgment_date.data)
    #     if data.is_valid():
    #         data.save()
    #         return Response(data.data)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)