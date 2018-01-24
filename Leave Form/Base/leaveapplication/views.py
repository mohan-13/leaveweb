from leaveapplication.forms import *
from .models import Students
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def home(request):
    return render(request,'leaveapplication/home.html')
def index(request):
    return render(request,'leaveapplication/index.html')
def apply(request):
    form1=StudentForm(request.POST)
    if form1.is_valid():
        user=form1.save()
    return render(request, 'leaveapplication/blog.html',{'form1': form1} )
def details(request):
    name=request.user.email
    data=Students.objects.filter(email=name)
    return render(request,'leaveapplication/details.html',{'data': data} )
def signup(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if password==confirm_password:
            form.save()
        else:
            form.add_error('confirm_password', 'The passwords do not match')

    else:
        form = SignUpForm()
    return render(request, 'leaveapplication/signup.html', {'form': form})


# Create your views here.
