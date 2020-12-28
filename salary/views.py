from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employee.models import Employee, Attendance
from .models import *
import datetime as dt
#from .classes import Payslip
# Create your views here.
def display(request):
    return render(request,'page.html')
'''
def edit_sal(request):
    if(request.method == 'GET'):
        #obj = Salary.objects.get(id=1)
        obj = Salary(emp=Employee.objects.get(id=1),date=dt.date.today())
        obj.save()
        return render(request,'edit.html',{'obj':obj})
    else:
        try:
            #wage = request.POST['wage']
            id = request.POST['id']
            claims = request.POST['claims']
            bonus = request.POST['bonus']
            obj = Salary.objects.get(emp=1,date=dt.date.today())
            
            if(obj.emp.base_sal!=wage):
               obj.emp.base_sal=wage
               obj.emp.save()
            obj.claims=claims
            obj.bonus=bonus
            obj.save()
            msg = "Salary updated"
        except Exception as e:
            msg='Failed to update'
        messages.info(request,msg)
        return redirect('/salary')

'''

def payslip(request,id):
    #id =2 #venki
    '''
    emp = Employee.objects.get(pk=id)
    salary = Salary.objects.get(employee_name=emp.id)
    overtime = 2'''

    payroll = Payroll.objects.all().get(emp=id,date=dt.date(2020,12,24))
    print(payroll.deduction.total_deductions)
    print(payroll.amount)


    return render(request,'payroll.html',{'obj':payroll})

def show(request):
    return render(request,'features.html')

def search(request):
    if request.method=='POST':
        name = request.POST['search']
        emp = Employee.objects.all().filter(name__icontains=name)
        print(emp)
        return render(request,'searchresults.html',{'obj':emp})
    else:
        return redirect('/')

def salaryslip(request):
    obj = Employee.objects.get(pk=2)
    return render(request,'salaryslip.html',{'obj':obj})

def loadatd(request):
    return render(request,'attendance.html')

def accountant(request):
    if request.user.groups.filter(name=user.name).exists():
        print("YEs")
    if request.user.is_authenticated:
        return render(request,'accountant.html')
    else:
        return redirect("")