from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import LatestNews


# Create your views here.
def index(request):
    return HttpResponse("Hello")

def help(request):
        dict={}
    
        return render(request,"help.html",dict)

def projform(request):
        dict={}
    
        return render(request,"projectform.html",dict)

def myprof(request):
        dict={}
    
        return render(request,"myprofile.html",dict)

def hlpsupp(request):
        dict={}
    
        return render(request,"help&support.html",dict)        
def edtprof(request):
        dict={}
    
        return render(request,"editprofile.html",dict) 
def chgpass(request):
        dict={}
    
        return render(request,"chngepass.html",dict)

def abtus(request):
        dict={}
    
        return render(request,"aboutUs.html",dict) 

def contact(request):
        dict={}
    
        return render(request,"aform5.html",dict) 
def rvw(request):
        dict={}
    
        return render(request,"review.html",dict)

def reg(request):
        dict={}
    
        return render(request,"register.html",dict)

def login(request):
        dict={}
    
        return render(request,"clientlogin.html",dict)

def news(request):      
   latestnews = LatestNews.objects.all()    
   return render(request,"viewLatestNews.html",{'latestnews':latestnews})  



