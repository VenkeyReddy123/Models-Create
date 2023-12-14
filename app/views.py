from django.shortcuts import render

# Create your views here.
from app.models import *
def Dis_Topic(request): 
    QSTO=Topic.objects.all()
    d={'topic':QSTO}
    return render(request,'Dis_Topic.html',d)
def Dis_Webpage(request):
    QSWO=WebPage.objects.all()
    d={'webpage':QSWO}
    return render(request,'Dis_Webpage.html',d)

def Dis_Dept(request):
    QSDO=Dept.objects.all()
    d={'dept':QSDO}
    return render(request,'Dis_Dept.html',d)
def Dis_Emp(request):
    QSEO=Employe.objects.all()
    d={'employe':QSEO}
    return render(request,'Dis_Emp.html',d)


