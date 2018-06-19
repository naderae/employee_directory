from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
from .forms import EmployeeForm
import json


# Create your views here.
def index(request):

    form = EmployeeForm()
    return render(request, 'employees/index.html', {'form': form})

def create_post(request):

    if request.method == 'POST':
        employee_name = request.POST.get('name')
        employee_title = request.POST.get('job_title')
        employee_experience = request.POST.get('years_experience')
        employee_department = request.POST.get('department')
        # employee_image = request.FILES.get('image')

        response_data = {}

        employee = Employee(name=employee_name, job_title=employee_title, years_experience=employee_experience, department=employee_department)
        employee.save()

        response_data['result'] = 'Added employee successfully!'
        response_data['employeepk'] = employee.pk
        response_data['name'] = employee.name
        response_data['job_title'] = employee.job_title
        response_data['years_experience'] = employee.years_experience
        response_data['department'] = employee.department
        # response_data['image'] = employee.image


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
