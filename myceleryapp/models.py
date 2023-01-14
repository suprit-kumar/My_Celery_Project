from django.db import models

# Create your models here.

class Storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=200, default='')
    address_1 = models.CharField(max_length=200, default='')
    address_2 = models.CharField(max_length=200, default='')
    region = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default="India")
    user = models.CharField(max_length=200, default="")
    datestamp = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "storage"
