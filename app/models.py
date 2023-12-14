from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Topic_Name
class WebPage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.URLField()
    Email=models.EmailField(default='India@123gamil.com')
    def __str__(self):
        return self.Name
class AccessRecord(models.Model):
    NAME=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)

class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    def __str__(selff):
        return selff.Dname

class Employe(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    HireDate=models.DateField()
    Salary=models.IntegerField()
    Comm=models.IntegerField(null=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(selff):
        return selff.Ename
class Salgrade(models.Model):
    Grade=models.IntegerField(primary_key=True)
    LSal=models.IntegerField()
    HSal=models.IntegerField()
    def __str__(selff):
        return str(selff.Grade)

class Bonus(models.Model):
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    def __str__(selff):
        return selff.Ename

class Countries(models.Model):
    Country_Name=models.CharField(max_length=100,primary_key=True)
class Capitals(models.Model):
    Country_Name=models.OneToOneField(Countries,on_delete=models.CASCADE)
    Capital_Name=models.CharField(max_length=100)






