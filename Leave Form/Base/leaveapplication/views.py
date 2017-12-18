from django.shortcuts import render
from django.http import HttpResponse
from leaveapplication.forms import *

def index(request):
    return HttpResponse(
        "<title>Home</title><h2> <p></p> <a href=""apply"" >Leave Apply </a>")
    #return render(request,'leaveapplication/index.html')
def tester(request):
    form1=StudentForm(request.POST)
    #if form1.is_valid():
        #text=form1.cleaned_data['firstname','lastname','email','date','reason']
    args={'form1': form1,}
    return render(request, 'leaveapplication/blog.html', args)

# Create your views here.
