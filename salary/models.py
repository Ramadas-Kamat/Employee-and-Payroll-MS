from django.db import models
from employee.models import Employee
from month.models import MonthField
# Create your models here.
class Payroll(models.Model):
    date = models.DateField(null=True)
    #month = MonthField(null=True)
    wages = models.FloatField(null=True,default=0)
    claims = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    deduction = models.ForeignKey('Deduction',on_delete=models.CASCADE,null=True)
    OT = models.ForeignKey('Overtime',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.date) + str(self.emp.name)
    
    class Meta:
        unique_together = ('emp','date')
    @property
    def amount(self):
        return self.wages + self.claims + self.bonus

    '''def get_wage(self):
        return emp.base_sal
    
    def set_wage(self,wage):
        employee = self.emp
        employee.base_sal=wage
        employee.save()'''

class Deduction(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = MonthField(null=True)
    #total_shifts = models.IntegerField(default=0)
    remaining_shifts = models.IntegerField(default=0)

    class Meta:
        unique_together=('emp_id','month')
    
    def __str__(self):
        return str(self.emp_id.name)+str(self.month)

    '''@property
    def total_deductions(self):
        #hard coded 100 but must come from pay per shift
        return (self.total_shifts - self.remaining_shifts)*100  
        '''

class Overtime(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = MonthField(null=True)
    OT_shifts = models.IntegerField(default=0)
    #OT_pay = models.FloatField(default=0)

    def __str__(self):
        return str(self.emp_id.name)+str(self.month)
    
    class Meta:
        unique_together=('emp_id','month')
    
    @property
    def OT_pay(self):
        #30 is hard coded must come from pay per shift
        return self.OT_shifts*30

class Salary(models.Model):
    employee_name  = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False)
    base_sal = models.FloatField(default=0,blank=False)
    pay_per_shift = models.FloatField(default=0,blank=False)

    def __str__(self):
        return str(self.base_sal)