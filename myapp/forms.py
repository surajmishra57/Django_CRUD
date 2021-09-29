from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        labels = {'name': "Name", 'email': 'Email', 'password': 'Password'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.TextInput(attrs={'class': 'form-control'})
                   }
