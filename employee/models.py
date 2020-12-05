from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from .models2 import Worksite
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    doj = models.DateField()
    work = models.ForeignKey('Worksite',on_delete=models.CASCADE, null=True)
    base_sal = models.FloatField(default=0)
    supervisor = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    #salary = models.OneToOneField(Salary,on_delete= models.CASCADE,null=True)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name','doj')

class Worksite(models.Model):
    name = models.CharField(max_length=20)       
    location = models.CharField(max_length=20)
    address = models.TextField(max_length=35)
    manager = models.ForeignKey(Employee,on_delete=models.CASCADE)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    in_time = models.TimeField()
    out_time = models.TimeField()
    worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    class Meta:
        unique_together = ('emp_id','date')
    
    

class Category(models.Model):
    name = models.CharField(max_length=15)
    
