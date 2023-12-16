from django.contrib import admin
from django.urls import path,include
from vendor.views import Purchase_OrdersView
# VendorViewSet,
# from rest_framework import routers
from vendor import views

# router = routers.DefaultRouter()
# # # router.register(r'vendors',VendorViewSet)
# router.register(r'puchase_orders',Purchase_OrdersView)

urlpatterns = [
    # path('',include(router.urls)),
    path('names/',views.Purchase_OrdersView.as_view(),name='posts'),
    path('lists/',views.Purchase_OrdersView.as_view(),name='lists')

]
