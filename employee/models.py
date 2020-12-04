from django.db import models
from salary.models import Salary
#from .models2 import Worksite
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    doj = models.DateField()
    work = models.ForeignKey('Worksite',on_delete=models.CASCADE, null=True)
    salary = models.OneToOneField(Salary,on_delete= models.CASCADE,null=True)
    class Meta:
        ordering = ('id','name','doj')

class Worksite(models.Model):
    name = models.CharField(max_length=20)       
    location = models.CharField(max_length=20)
    address = models.TextField(max_length=35)
    manager = models.ForeignKey(Employee,on_delete=models.CASCADE)



class Attendance(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    in_time = models.TimeField()
    out_time = models.TimeField()
    worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    class Meta:
        unique_together = ('emp_id','date')

