from django.db import models

# Create your models here.

class mult(models.Model):
    lid=models.IntegerField(primary_key=True)
    count=models.CharField(max_length=30)
class speaker(models.Model):
    lid=models.IntegerField()
    speak = models.FileField()
    num=models.IntegerField()