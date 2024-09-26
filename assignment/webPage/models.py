from django.db import models

# Create your models here.
class userInfo(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Address=models.CharField(max_length=500)
    MobNO=models.CharField(max_length=11)
