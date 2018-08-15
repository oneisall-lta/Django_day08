from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from homework.models import *


def go_grade(req):
    return render(req, 'addgrade.html')


def go_stu(req):
    grades = Grade.objects.all()
    return render(req, 'addstu.html', locals())


def addgrade(request):
    c_grade = request.POST.get('grade')
    print(c_grade)
    Grade.objects.create(gname=c_grade)
    return render(request, 'addgrade.html')


def addstu(request):
    banji = request.POST.get("grade")
    name = request.POST.get('stuname')
    sex = request.POST.get('sex')
    age = request.POST.get('stuage')

    # banji_id = Grade.objects.filter(gname=banji)[0].id  # filter查询的是一组对象，当gname有重名的，此方法就不适用。
    print(banji, name, sex, age)

    Student.objects.create(stuname=name, age=age, sex=sex, grade_id=banji)

    return HttpResponseRedirect('showstu.html')


def show_student(req):
    students = Student.objects.all()
    return render(req,'showstu.html',{'students': students})
