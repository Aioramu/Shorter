from django.db import models

# Create your models here.
class Urls(models.Model):
    initial=models.CharField(max_length=100,default="")
    final=models.CharField(max_length=100,default="")
