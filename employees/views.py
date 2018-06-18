from django.shortcuts import render
from employees.models import Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):

    form = EmployeeForm()


    return render(request, 'employees/index.html', {'form': form})
