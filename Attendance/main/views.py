from django.shortcuts import render, redirect
import sqlite3
from main.models  import Member, Attendance #모델의 존재 알려주기

# Create your views here.

def main(request):

    return render(request,'produce.html')

def chk(request):
    #폼 입력값 가져오기
    attendance=Attendance()
    attendance.name=request.POST['name']
    attendance.attendance=request.POST['attendance']
    attendance.date=request.POST['date']
    names=Member.objects.all()
    
    attendance.save()
    
    return render(request,'main.html',{'date':attendance.date,'names':names})

def date(request):
    #폼 입력값 가져오기
    date=request.POST['date']
    names=Member.objects.all()
    
    return render(request,'main.html',{'date':date,'names':names})

def show(request):

    return render(request,'show.html')

def show1(request):

    date=request.POST['date']
    
    info = Attendance.objects.filter(date__contains='{}'.format(date))

    return render(request,'show1.html',{'info':info})