from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import data
from django.contrib.auth import authenticate,login

from django.contrib import auth
#from django.contrib.auth.models import data,auth


#from .models import data,auth

def fun1(request):
    return render(request,'first.html')

def fun2(request):
    return render(request,'register.html')

def fun3(request):
    if request.method=="POST":
        s1=request.POST['us']
        if data.objects.filter(name=s1).exists():
            messages.info(request,'username alredy exit')
            return render(request,'register.html')
        else:
            s2=request.POST['pa']
            s3=request.POST['em']
            s4=request.POST['ph']
            dd=data(name=s1,password=s2,email=s3,phone=s4)
            dd.save()
        #print('user save')
            return render(request,'login.html')

def fun4(request):
    return render(request,'login.html')

def fun5(request):
    if request.method=="POST":
         a=request.POST['um']
         b=request.POST['pp']
         if data.objects.filter(name=a,password=b):
             return HttpResponse('suc')
         
         #if data is not None:
             #auth.login(request,data)
             #return render(request,'result.html')
         else:
             #messages.info(request,'invalid username and password')
             return HttpResponse('unsuc')

    else:
        return render(request,'first.html')
         


