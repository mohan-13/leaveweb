from django import forms
from leaveapplication.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

    def __init__(self, user,*args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.user = user
    class Meta:
        model=Students
        fields=['reason','from_date','to_date']
    def save(self,commit=True):
        data=self.cleaned_data

        f_date=data['from_date']
        t_date=data['to_date']
        reason=data['reason']

        student = Students.objects.create(to_date=t_date,from_date=f_date,reason=reason,apply_user=self.user)
        return student
class AdminForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['status']
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255,)

    class Meta:
        model = user

        fields = ('rollno', 'first_name', 'email', 'password', 'confirm_password',)

    def save(self, commit=True):
        data = self.cleaned_data
        password = data['password']
        first_name = data['first_name']
        rollno = data['rollno']
        email = data['email']
        user_obj = User.objects.create_user(username=email, email=email, first_name=first_name, password=password)
        user.objects.create(rollno=rollno, foreign_user=user_obj)
        return user_obj



