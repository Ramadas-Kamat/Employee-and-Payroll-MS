from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import * #Employee, Attendance, Worksite, Category
import datetime
from django.http import Http404  
#import Exception
# Create your views here.

def display(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        pd1 = request.POST['psd']
        pd2 = request.POST['cpsd']
        mail = request.POST['mail']
        un = request.POST['user_name']
       # user = User.objects.create_user()
       # user.save()
        msg =""
        if pd1 == pd2:
            if User.objects.filter(username=un).exists():
                msg = "Uname exists"
            elif User.objects.filter(email = mail).exists():
                msg = 'Mail exists'
                print("Mail exists")
            else:
                user = User.objects.create_user(username = un,first_name=fn,last_name=ln,\
                email=mail,password=pd1)
                user.save()
                print("User created")
                auth.login(request,user)
                return redirect('/')
        else:
           msg ="Passwords dont match"
        messages.info(request,msg)
        return redirect("register")
        
        
    else:
        return render(request,'userform.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        psd = request.POST['psd']

        user  = auth.authenticate(username = uname, password =psd)
        print(user)
        if user!=None:
            auth.login(request,user)
            return redirect('/emplogin')
        else:
            messages.info(request,"Incorrect username or password")
            return redirect('login')
    else:
        return render(request,'login.html')
'''
def create_emp(request):
    msg=''
    try:
        val = request.POST['val']
        if val==1:
            emp = Employee()
            emp.name="Ramadas"
            emp.sex='Male'
            emp.doj = datetime.date
            emp.save()
            msg = 'Successfull'
            print('DONE')
            #logout(request)
    except Exception as er: #MultiValueDictKeyError
        msg = 'In exception'
    messages.info(request,msg)
    return render(request,'emp.html')'''

def search(request):
    name = request.POST['search']
    try:
        #Better for prefixes
        obj = Employee.objects.filter(name__icontains=name)[0]  
        atd = Attendance.objects.filter(emp_id= obj.id)
        return render(request,'details.html',{'obj':obj,'atd':atd})
    
    except Exception as e:
        exc = "No employee named " + name
        print(e)
        #return render(request, 'exception.html',{'exc':exc})
        messages.info(request, exc)
        return redirect('/')

def loader(request):
    
    atd = Attendance.objects.filter(date='2020-12-4')
    obj = atd.count()
    query = atd.query
    
    return render(request,'load.html',{'query':query,'ans':obj})
    #return render(request,'index1.html')

def show_attendance(request,id):
    atd = Attendance.objects.filter(emp_id=id)
    emp = Employee.objects.get(pk=id)
    print(atd)
    return render(request,'attendanceview.html',{'objects':atd,"emp":emp})

def empview(request):
    if request.user.is_authenticated:
        print("Yes")
        emp = Employee.objects.get(pk=2)
        return render(request,'employee.html',{'emp':emp})
    else:
        print('No')
        raise Http404
        
        return None

def atdsearch(request):
    if request.method=='POST':
        name = request.POST['search']
        emp = Employee.objects.all().filter(name__icontains=name)
        print(emp)
        return render(request,'attendanceresults.html',{'obj':emp})
    else:
        return redirect('/')
    