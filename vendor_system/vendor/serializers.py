from rest_framework import serializers
# from vendor.models import Vendors
from vendor.models import Purchase_Orders

#  create Serializer

# class VendorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Vendors
#         fields="__all__"

class Purchase_OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Orders
        fields = "__all__"