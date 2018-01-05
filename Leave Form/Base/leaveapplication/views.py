from django.shortcuts import render
from django.http import HttpResponse
from leaveapplication.forms import *
from .models import Students

def index(request):
    #return HttpResponse(
        #"<title>Home</title><h2> <p></p> <a href=""apply"" >Leave Apply </a>")
    return render(request,'leaveapplication/index.html')
def tester(request):
    form1=StudentForm(request.POST)
    if form1.is_valid():
        form1.save()
    return render(request, 'leaveapplication/blog.html',{'form1': form1} )
def details(request):
    data=Students.objects.all()
    return render(request,'leaveapplication/details.html',{'data': data} )

# Create your views here.
