from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_Name=models.CharField(max_length=100)
class WebPage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.URLField()
class AccessRecord(models.Model):
    NAME=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)
