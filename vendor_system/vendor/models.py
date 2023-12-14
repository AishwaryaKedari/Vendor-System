from django.db import models

# Create your models here.

# Creating Vendor Profile model


class Vendors(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=12, unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

# Creating Purchase Order Tracking model
#  Model Design: Track purchase orders with fields like PO number, vendor reference,
# order date, items, quantity, and status.

class Purchase_Orders(models.Model):
     po_number = models.CharField(max_length=20,unique=True)
     vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE)
     order_date = models.DateTimeField()
     delivery_date = models.DateTimeField()
     items = models.JSONField()
     quantity = models.IntegerField()
     status = models.CharField(max_length=20)
     quality_rating = models.FloatField(null=True,blank=True)
     issue_date = models.DateTimeField()
     acknowledgment_date = models.DateTimeField(auto_now=True,null = True,blank=True)

