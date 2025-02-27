from django.db import models
from Guest.models import * 
from Shop.models import *

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)

class tbl_booking(models.Model):
     booking_date = models.DateField(auto_now_add=True)
     booking_totalamount = models.CharField(max_length=30)
     booking_adv_amount = models.CharField(max_length=30)
     booking_status = models.IntegerField(default=0)
     user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)



