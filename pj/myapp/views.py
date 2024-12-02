from django.shortcuts import render
from .models import course

def course_list(request):
    list = course.objects.all()
    return render(request,'course.html',{'course':list})