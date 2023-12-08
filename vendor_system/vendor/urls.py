from django.contrib import admin
from django.urls import path,include
from vendor.views import VendorViewSet,Purchase_OrdersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'vendors',VendorViewSet)
router.register(r'puchase_orders',Purchase_OrdersViewSet)

urlpatterns = [
    path('',include(router.urls)),

]
