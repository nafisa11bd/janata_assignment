from django.db import models

# Create your models here.
class stockinfo(models.Model):
    date=models.CharField(max_length=100)
    trade_code=models.CharField(max_length=200)
    high=models.CharField(max_length=100)
    low=models.CharField(max_length=100)
    open=models.CharField(max_length=100)
    close=models.CharField(max_length=100)
    volume=models.CharField(max_length=100)

