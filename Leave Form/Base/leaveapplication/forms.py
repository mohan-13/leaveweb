from django import forms
from leaveapplication.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['firstname','lastname','email','date','reason',]
