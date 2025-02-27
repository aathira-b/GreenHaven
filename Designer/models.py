from django.db import models
from Guest.models import *

# Create your models here.

class tbl_work(models.Model):
   work_name=models.CharField(max_length=50)
   work_photo=models.FileField(upload_to='Assets/designer/photo/')   
   work_details=models.CharField(max_length=50)

class tbl_gallery(models.Model):
   designer_id=models.ForeignKey(tbl_designer,on_delete=models.CASCADE)
   gallery_photo=models.FileField(upload_to='Assets/designer/photo/')   

