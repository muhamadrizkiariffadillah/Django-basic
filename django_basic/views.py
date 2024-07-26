from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.filter()
    context = {
        'employee':employees,
    }
    return render(request,'index.html',context)

