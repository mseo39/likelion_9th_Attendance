from django.db import models

# Create your models here.

class Member(models.Model): #모델명의 첫글자는 대문자로
    name = models.CharField(max_length = 50) #최대로 넣을 수 있는 글자 수
    student_id = models.CharField(max_length = 50)
    major = models.CharField(max_length = 50, null=True)
    attendance = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)
    tardy = models.IntegerField(default=0)
    etc = models.IntegerField(default=0)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.name

class Attendance(models.Model): #모델명의 첫글자는 대문자로
    name = models.CharField(max_length = 50) #최대로 넣을 수 있는 글자 수
    attendance = models.CharField(max_length = 50)
    date = models.CharField(max_length = 50)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.name