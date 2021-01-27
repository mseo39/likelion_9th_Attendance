from django.shortcuts import render, redirect, get_object_or_404
import sqlite3
from main.models  import Member, Attendance #모델의 존재 알려주기
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker

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

    member_info.save()
    attendance.save()

    return render(request,'attendance.html',{'date':attendance.date,'names':names})

def date(request):
    #폼 입력값 가져오기
    date=request.POST['date']
    names=Member.objects.all()
    
    return render(request,'attendance.html',{'date':date,'names':names})

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

    return render(request, 'member.html', {'names':names,'member_name':member_name,'data':data,'name':name})

def return_graph(name_id):

    name=get_object_or_404(Member, pk=name_id)
   
    fig = plt.figure(figsize=(4, 2.2))

    path = 'main/font/12롯데마트드림Medium.ttf'
    fontprop = fm.FontProperties(fname=path, size=11)

    x=np.arange(4) #주어진 범위와 간격에 따라 균일한 값을 갖는 어레이를 생성하는 함수
    valuetype=['출석','결석','지각','기타'] #x축에 표시될
    values=[name.attendance, name.absent, name.tardy, name.etc] #막대 그래프의 높이로 표시될 y 값 
    plt.bar(x,values)
    plt.xticks(x, valuetype, fontproperties=fontprop)

    ax=plt.axes()
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
