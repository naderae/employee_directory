from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'years_experience', 'department')
        labels = {
            'years_experience': ('years of experience')
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'employee-name', 'required': True, 'placeholder': 'Employee name...'}
            ),
            'job_title': forms.TextInput(
                attrs={'id': 'employee-job-title', 'required': True, 'placeholder': 'Employee title'}
            ),
            'years_experience': forms.NumberInput(
                attrs={'id': 'employee-years-experience', 'required': True, 'placeholder': 'Years of experience...'}
            ),
            'department': forms.Select(
                attrs={'id': 'employee-department', 'required': True, 'placeholder': 'department...'}
            ),
            # 'image': forms.FileInput(
            #     attrs={'id': 'employee-image', 'required': True}
            # ),
        }
