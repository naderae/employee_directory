from django.shortcuts import render
from employees.models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects
    return render(request, 'employees/index.html')
