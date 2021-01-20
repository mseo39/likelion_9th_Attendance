from django.shortcuts import render, redirect
import sqlite3
from main.models  import Member #모델의 존재 알려주기

# Create your views here.

def main(request):

    name=Member.objects.all()
    return render(request,'main.html',{'name':name})

def chk(request):
    #폼 입력값 가져오기
    name=request.POST['name']
    attendance=request.POST['attendance']
    
    #데이터베이스 연결
    conn=sqlite3.connect('member.db')
    cursor=conn.cursor()
    #데이터베이스 등록(삽입)
    cursor.execute('''
    insert into meminfo (name,attendance) values(?,?)''',(name,attendance))
    conn.commit()
    conn.close()
    
    return redirect('main') #login.html파일 렌더링