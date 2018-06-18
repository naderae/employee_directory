from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'years_experience', 'department', 'image',)
        labels = {
            'years_experience': ('years of experience')
        }
        # widgets = {
        #     'years_experience': forms.TextInput(
        #         attrs={'id': 'post-name', 'required': True, 'placeholder': 'My name is...'}
        #     ),
        #     'job_title': forms.TextInput(
        #         attrs={'id': 'post-job-title', 'required': True, 'placeholder': 'My current title...'}
        #     ),
        #     'experience': forms.TextInput(
        #         attrs={'id': 'post-experience', 'required': True, 'placeholder': 'Years of experience...'}
        #     ),
        # }
