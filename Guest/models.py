
# Create your models here.
from django.db import models
from Admin.models import *

class tbl_user(models.Model):
   user_name=models.CharField(max_length=50)
   user_email=models.CharField(max_length=50)
   user_address=models.CharField(max_length=50)
   user_contact=models.CharField(max_length=50)
   user_password=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   user_photo=models.FileField(upload_to='Assets/user/photo/')

class tbl_designer(models.Model):
   designer_name=models.CharField(max_length=50)
   designer_email=models.CharField(max_length=50)
   designer_address=models.CharField(max_length=50)
   designer_contact=models.CharField(max_length=50)
   designer_password=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   designer_photo=models.FileField(upload_to='Assets/designer/photo/')   
   designer_proof=models.FileField(upload_to='Assets/designer/photo/') 
   designer_status=models.IntegerField(default=0)    

class tbl_shop(models.Model):
   shop_name=models.CharField(max_length=50)
   shop_email=models.CharField(max_length=50)
   shop_address=models.CharField(max_length=50)
   shop_contact=models.CharField(max_length=50)
   shop_password=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   shop_logo=models.FileField(upload_to='Assets/shop/photo/')   
   shop_license=models.FileField(upload_to='Assets/shop/photo/')  
   shop_status=models.IntegerField(default=0) 

