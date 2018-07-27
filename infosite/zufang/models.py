from django.db import models


# Create your models here.
class Zufang_Info(models.Model):
    title = models.CharField(max_length=200)
    month_money = models.CharField(max_length=100)
    mianji = models.CharField(max_length=200)
    img = models.CharField(max_length=300, default="")
    next_url = models.CharField(max_length=200, default="")
    jjr_img = models.CharField(max_length=300,default="")
    jjr = models.CharField(max_length=200,default="")
    jjr_phone = models.CharField(max_length=200,default="")
    address = models.CharField(max_length=200,default="")
    city_address = models.CharField(max_length=200,default="")
class Zufang_content_Info(models.Model):
    info_id = models.IntegerField(primary_key=True, db_column='FId', default=1)
    jjr_img = models.CharField(max_length=300)
    jjr = models.CharField(max_length=200)
    jjr_phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
