from distutils.command.upload import upload
from operator import imod
from sqlite3 import Timestamp
from django.db import models
import barcode
from io import BytesIO
from barcode.writer import ImageWriter
from django.core.files import File

# Create your models here.
class stock_tracking_model(models.Model):
    BarCode = models.IntegerField("",default=0000000000000)
    product_id = models.IntegerField()
    prod_description = models.CharField(max_length=100)
    product_code_1 = models.IntegerField()
    product_code_2 = models.IntegerField()

class product_model(models.Model):
    Barcode = models.IntegerField()
    product_code = models.IntegerField()
    no_of_cartons = models.IntegerField()
    barcode_image = models.ImageField(upload_to='images/',blank =True)
    Timestamp = models.DateTimeField(auto_now=True)

    
    def save(self,*args,**kwargs):
        pr=barcode.get_barcode_class('EAN13')
        Ean = pr(f"{self.Barcode}099",ImageWriter())
        buffer = BytesIO()
        Ean.write(buffer)
        self.barcode_image.save(f"{self.product_code}.png",File(buffer),save=False)
        return super().save(*args,**kwargs)


