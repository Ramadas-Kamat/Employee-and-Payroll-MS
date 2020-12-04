from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employee.models import Employee, Attendance
from .models import Salary
# Create your views here.
def display(request):
    return render(request,'page.html')

def edit_sal(request):
    if(request.method == 'GET'):
        obj = Salary.objects.get(id=1)

        return render(request,'edit.html',{'obj':obj})
    else:
        try:
            wage = request.POST['wage']
            id = request.POST['id']
            claims = request.POST['claims']
            bonus = request.POST['bonus']
            obj = Salary.objects.get(id=1)
            obj.wages = wage
            obj.claims=claims
            obj.bonus=bonus
            obj.save()
            msg = "Edited successfully"
        except Exception as e:
            msg='Failed to update'
        messages.info(request,msg)
        return redirect('/salary')