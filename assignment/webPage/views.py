from django.shortcuts import render,redirect
import datetime
import time
from .form import userinfo
from webPage.models import userInfo
# Create your views here.
def home(request):
    dt=datetime.datetime.now()
    today_date=datetime.date.today()
    time=datetime.datetime.now()
    hour=time.hour
    min=time.minute
    sec=time.second
    
    
    
    if request.method == "POST":
        form = userinfo(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('userInfo')  
        else:
            print(form.errors)

    else:
        form = userinfo()
    
    

   
    

    date={
        'datetime':dt,
        'date':today_date,
        'hour':hour,
        'min':min,
        'sec':sec,
        'form':form,
    }
    
    return render(request,'homepg.html',date) 

def user_Info(request):
     

    user = userInfo.objects.all()
    l=list(userInfo.objects.all())
    last=(l[-1])
    
    name=last.Name
    mail=last.email
    add=last.Address
    no=last.MobNO
    return render(request, 'user_info.html',{ 'user':user,'l':l,'last':last, 'name':name,'mail':mail,'add':add,'no':no})
    