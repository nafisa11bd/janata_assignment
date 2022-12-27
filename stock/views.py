from django.shortcuts import render
from .models import stockinfo
from django.contrib import messages
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from .utils import get_plot
from .utils import get_barplot
matplotlib.use("Agg")

# Create your views here.
def index(request):
    stockInfo=stockinfo.objects.all()
    qs=stockinfo.objects.all()
    x=[]
    x1=[]
    y=[]
    y1=[]
    j=0
    for i in qs:
        j=j+1
        if j <= 500:
             x.append(i.trade_code)
             #x1.append(i.date)
             y.append(float(i.close))
             y1.append(int(i.volume.replace(',', '')))
             print(int(i.volume.replace(',', '')))
             
    
    chart=get_plot(x,y)
    chart2=get_barplot(x,y1)
    diction={'stockInfo':stockInfo,'chart':chart,'chart2':chart2}
    return render(request,'stock/index.html',context=diction)
    print(3)
def create(request):
    if request.method=="POST":
        if request.POST.get('date') and request.POST.get('trade_code') and request.POST.get('high') and request.POST.get('low') and request.POST.get('open') and request.POST.get('close') and request.POST.get('volume'):
            savestock=stockinfo()
            savestock.date=request.POST.get('date')
            savestock.trade_code=request.POST.get('trade_code')
            savestock.high=request.POST.get('high')
            savestock.low=request.POST.get('low')
            savestock.open=request.POST.get('open')
            savestock.close=request.POST.get('close')
            savestock.volume=request.POST.get('volume')
            savestock.save()
            return render(request,'stock/create.html')
    else:
            return render(request,'stock/create.html')        

def edit(request,id):
    getstockdetails=stockinfo.objects.get(id=id)
    return render(request,'stock/edit.html',{"stockinfo":getstockdetails})
def delete(request,id):
    deletestock=stockinfo.objects.get(id=id)
    deletestock.delete()
    result=stockinfo.objects.all()
    return render(request,'stock/index.html',{"stockinfo":result})
def graph(request):
    qs=stockinfo.objects.all()
    x=[]
    x1=[]
    y=[]
    y1=[]
    j=0
    for i in qs:
        j=j+1
        if j <= 500:
             x.append(i.trade_code)
             #x1.append(i.date)
             y.append(float(i.close))
             y1.append(int(i.volume.replace(',', '')))
             print(int(i.volume.replace(',', '')))
             
    
    chart=get_plot(x,y)
    chart2=get_barplot(x,y1)
    return render(request,'stock/index.html',{'chart':chart,'chart2':chart2})



