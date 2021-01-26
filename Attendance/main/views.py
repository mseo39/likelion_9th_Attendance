from django.shortcuts import render, redirect, get_object_or_404
import sqlite3
from main.models  import Member, Attendance #모델의 존재 알려주기
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

# Create your views here.

def main(request):

    return render(request,'produce.html')

def member(request):
    names=Member.objects.all()
    return render(request,'member.html',{'names':names})

def chk(request):
    #폼 입력값 가져오기
    attendance=Attendance()
    attendance.name=request.POST['name']
    attendance.attendance=request.POST['attendance']
    attendance.date=request.POST['date']
    names=Member.objects.all()
    name=request.POST['name']

    member_info=get_object_or_404(Member, name=name)
    if attendance.attendance=="출석":
        member_info.attendance+=1
    
    elif attendance.attendance=="결석":
        member_info.absent+=1
    
    elif attendance.attendance=="지각":
        member_info.tardy+=1

    elif attendance.attendance=="기타":
        member_info.etc+=1

    member1.save()
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

def detail(request, name_id):
    names=Member.objects.all()
    name=get_object_or_404(Member, pk=name_id)
    member_name = Attendance.objects.order_by('-date').filter(name__contains='{}'.format(name.name))

    data = return_graph(name_id)

    return render(request, 'member.html', {'names':names,'member_name':member_name,'data':data})

def return_graph(name_id):

    name=get_object_or_404(Member, pk=name_id)
   
    fig = plt.figure()

    x=np.arange(4) #주어진 범위와 간격에 따라 균일한 값을 갖는 어레이를 생성하는 함수
    valuetype=['attendance','absent','tardy','etc'] #x축에 표시될
    values=[name.attendance, name.absent, name.tardy, name.etc] #막대 그래프의 높이로 표시될 y 값 
    plt.title("attendance")
    plt.bar(x,values)
    plt.xticks(x, valuetype)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
