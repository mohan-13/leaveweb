from django import forms
from leaveapplication.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

    class Meta:
        model=Students
        fields=['reason',]
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model = user

        fields = ('rollno', 'firstname', 'lastname', 'email', 'password','confirm_password',)



