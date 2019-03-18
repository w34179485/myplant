from django.db import models

class Merchandise(models.Model):
    mer_number = models.CharField(max_length=200)
    mer_name  = models.CharField(max_length=200)
    mer_type = models.CharField(max_length=200)

class Detail(models.Model):
    merchandise = models.ForeignKey(Merchandise,on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    producer = models.CharField(max_length=200)