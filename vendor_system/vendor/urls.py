from django.urls import path,include
# from vendor.views import Purchase_OrdersView
from rest_framework.routers import DefaultRouter
from vendor import views

# router = DefaultRouter()
# router.register('purchase_orders',views.Purchase_OrdersView,basename='purchase_orders')

urlpatterns = [
    # patterns('vendor.views',url(r'^pots/{id}','post'),)
    # path('PO/',views.Purchase_OrdersView.as_view()),
    # path('',include(router.urls))
    path('purchase_orders/',views.Purchase_OrdersView.as_view()),
]
    
