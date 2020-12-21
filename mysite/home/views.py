from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home/homepage.html')


def student(request):
    return render(request, 'home/student.html')


def teacher(request):
    return render(request, 'home/teacher.html')


def login(request):
    return render(request, 'home/login.html')


def edit(request):
    return render(request, 'home/edit.html')