from leaveapplication.forms import *
from .models import Students
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect , redirect
from django.contrib import messages

def home(request):
    return render(request,'leaveapplication/home.html')
def index(request):
    name = request.user.id
    name1 = request.user.first_name
    if name == 4:
        return render(request, 'leaveapplication/adminindex.html', {'user':name1})
    else:

        return render(request, 'leaveapplication/index.html', {'user':name1})
def apply(request):
    form = StudentForm(request.user)
    if request.method =="POST":
        form = StudentForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Leave Applied SucessFully")
            return redirect('index')

    return render(request, 'leaveapplication/blog.html',{'form1': form} )

def details(request):
    name=request.user.id
    name1 = request.user.first_name
    if name==4:
        data1=Students.objects.filter(status="SUBMITTED")
        select_value=request.POST.get('select_value')
        id=request.POST.get('id')
        try:
            leave_obj = Students.objects.get(id=id)
            if int(select_value) == 0:
                pass
            elif int(select_value) == 1:
                leave_obj.status = "APPROVED"
                leave_obj.save()
            elif int(select_value) == 3:
                leave_obj.status = "DENIED"
                leave_obj.save()
        except Students.DoesNotExist:
            pass
        return render(request, 'leaveapplication/admindetails.html', {'user': name1, 'data1': data1,})


    else:

        data=Students.objects.filter(apply_user_id=name)
        return render(request,'leaveapplication/details.html',{'user':name1,'data': data} )
def signup(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if password==confirm_password:
            form.save()
            return redirect('login')
        else:
            form.add_error('confirm_password', 'The passwords do not match')

    else:
        form = SignUpForm()
    return render(request, 'leaveapplication/signup.html', {'form': form})


# Create your views here.
