from django.db import models
from Guest.models import * 
from Admin.models import * 

# Create your models here.
class tbl_product(models.Model):
   subcategory_id=models.ForeignKey(tbl_subcat,on_delete=models.CASCADE)
   product_name=models.CharField(max_length=50)
   product_details=models.CharField(max_length=50)
   product_price=models.CharField(max_length=50)
   product_photo=models.FileField(upload_to='Assets/shop/photo/')
   shop = models.ForeignKey(tbl_shop, on_delete=models.CASCADE)

class tbl_stock(models.Model):
   product_id=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
   stock_quantity=models.CharField(max_length=50)
   stock_date=models.DateField(auto_now_add=True)
