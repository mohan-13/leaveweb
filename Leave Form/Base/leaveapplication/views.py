from leaveapplication.forms import *
from .models import Students
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def index(request):
    return render(request,'leaveapplication/index.html')
def tester(request):
    form1=StudentForm(request.POST)
    if form1.is_valid():
        form1.save()
    return render(request, 'leaveapplication/blog.html',{'form1': form1} )
def details(request):
    data=Students.objects.all()
    return render(request,'leaveapplication/details.html',{'data': data} )
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SignUpForm()
    return render(request, 'leaveapplication/signup.html', {'form': form})


# Create your views here.
