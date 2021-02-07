from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import re
from django.core.exceptions import ValidationError
from month.models import MonthField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
#from .models2 import Worksite
# Create your models here.
GENDER = [('Male','Male'),('Female','Female')]
TYPE = [('temp','Temporary'),('perm','Permanent'),('mng','Managerial')]
class Employee(models.Model):

    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=30,null=True,verbose_name='Last name')
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sex = models.CharField(max_length=10,choices=GENDER)
    doj = models.DateField(verbose_name='Date of Joining')
    work = models.ForeignKey('Worksite',on_delete=models.CASCADE, null=True,verbose_name="Worksite")
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)
    base_sal = models.FloatField(default=0)
    supervisor = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    #salary = models.OneToOneField(Salary,on_delete= models.CASCADE,null=True)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    image = models.ImageField(upload_to="profpics",null=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name','doj')
    
    def get_employee(id):
        return Employee.objects.get(id=id)
    
    def clean_fields(self,exclude=None):
        print("Hi in clean")
        pattern = r'[^A-Za-z]'
        flag1=flag2=False
        try:
            if re.findall(pattern,self.name) != [] :
                
                flag1=True
                raise ValidationError({'name':_('Incorrect name')})
            if re.findall(pattern,self.lname) != [] :
                
                flag2=True
                raise ValidationError({'lname':_('Incorrect lastname')})
            
            if flag1 and flag2:
                raise ValidationError({
            'name':ValidationError(_("Incorrect first name")),
            'lname':ValidationError(_("Incorrect last name"))
            })
        except:
            pass
        

    @property
    def worksite(self):
        return self.work
    
    @property
    def pps(self):
        pass

class Worksite(models.Model):
    name = models.CharField(max_length=20)       
    location = models.CharField(max_length=20)
    address = models.TextField(max_length=150)
    manager = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name
    
    def clean_fields(self,exclude=None):
        print("Hi in clean of worksite")
        pattern = r'[^A-Za-z]'
        try:
            if re.findall(pattern,self.name) != [] :
                raise ValidationError({'name':_("Invalid name")})
        except:
            pass

class Attendance(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    in_time = models.TimeField()
    out_time = models.TimeField()
    #worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    #class Meta:
        #unique_together = ('emp_id','date')
    
   
    @property
    def hours(self):
        end_minutes = self.out_time.hour*60 + self.out_time.minute
        start_minutes = self. in_time.hour*60 + self.in_time.minute
        return round((end_minutes - start_minutes) / 60,2)
    

    def clean_fields(self,exclude=None):
        if self.in_time > self.out_time:
            raise ValidationError("Provide valid time punches")
    def __str__(self):
        return str(self.emp_id.name)+' '+str(self.date)
    
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=15)
    num_of_emp = models.IntegerField(default=0,null=True,blank=True)
    type = models.CharField(max_length=10,choices=TYPE,null=True)

    def __str__(self):
        return str(self.name)
    def clean_fields(self,exclude=None):
        pattern = r'[^A-Za-z]'
        try:
            if re.findall(pattern,self.name) != [] :
                raise ValidationError({'name':_("Invalid name provided")})
        except:
            pass
    
    

class LabourHour(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    #hours = models.FloatField(default=0)
    #overtime_hours=models.IntegerField(default=0)
    unrecorded_hours = models.IntegerField(default=0)
    class Meta:
        unique_together = ('emp_id','date')

    def __str__(self):
        return str(self.emp_id.name)+str(self.date)
    
    @property
    def hours(self):
        #Get sum of all atd tuples for that day.
        atd = Attendance.objects.filter(emp_id=self.emp_id,date=self.date)
        sum=0
        for a in atd:
            sum+=a.hours
        return sum
    
    @property
    def total_shifts(self):
        val= (self.hours+self.unrecorded_hours)/8 #1 shift=8 hr hard coded
        min = int(val)
        if(val-min <0.5):
            shifts = min
        else:
            shifts =min+0.5
        
        #return min(shifts,2.5)
        return shifts
    
    @property
    def overtime_shifts(self):
        shifts = self.total_shifts

        if(shifts>=1):
            return shifts-1
        else:
            return 0

class WorkingShift(models.Model):
    month = MonthField(null=False,blank=False)
    worksite = models.ForeignKey(Worksite,on_delete=models.CASCADE, null=False)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE, null=False)
    working_days = models.IntegerField(default=27)
    leaves_allowed = models.IntegerField(default=0)

    class Meta:
        unique_together = ('month','worksite','category')
    
    def __str__(self):
        return "Shift for" +str(self.category.name)+ str(self.month)

