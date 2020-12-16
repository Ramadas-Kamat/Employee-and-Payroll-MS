from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employee.models import Employee, Attendance
from .models import Salary
import datetime as dt
# Create your views here.
def display(request):
    return render(request,'page.html')

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
            
            '''if(obj.emp.base_sal!=wage):
               obj.emp.base_sal=wage
               obj.emp.save()'''
            obj.claims=claims
            obj.bonus=bonus
            obj.save()
            msg = "Salary updated"
        except Exception as e:
            msg='Failed to update'
        messages.info(request,msg)
        return redirect('/salary')


