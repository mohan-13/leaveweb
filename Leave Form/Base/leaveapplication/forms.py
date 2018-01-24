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
    first_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)

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



