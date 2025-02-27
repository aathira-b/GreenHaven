from django.db import models

# Create your models here.
class tbl_district(models.Model):
   district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=100)
class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50) 
    admin_password=models.CharField(max_length=50)
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=100) 
class tbl_place(models.Model):
   place_name=models.CharField(max_length=50)
   district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)  
class tbl_subcat(models.Model):
   subcat_name=models.CharField(max_length=50)
   category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)     

   
   
