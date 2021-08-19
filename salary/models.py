from django.db import models
<<<<<<< HEAD
from employee.models import Employee
from month.models import MonthField
=======
from employee.models import *
from month.models import MonthField
import datetime as dt
import month
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
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
<<<<<<< HEAD
        return self.wages + self.claims + self.bonus

    '''def get_wage(self):
=======
        '''
        wage = obj.wage
        benefits = obj.claims+obj.bonus
        deductions = obj.deduction. '''
        wage = Salary.getsalary(self.emp)
        self.wages=wage
        self.save()
        #print("base:", Salary.getsalary(self.emp))
        benefits = self.claims + self.bonus
        deductions = self.deduction.total_deductions
        ot = self.OT.OT_pay
        return wage+benefits-deductions+ot
    
    '''
    def get_wage(self):
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
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
<<<<<<< HEAD
        return str(self.emp_id.name)+str(self.month)

    '''@property
    def total_deductions(self):
        #hard coded 100 but must come from pay per shift
        return (self.total_shifts - self.remaining_shifts)*100  
        '''
=======
        return str(self.emp_id.name)+ ' '+str(self.month)

    @property
    def total_deductions(self):
        #hard coded 100 but must come from pay per shift
        #leave = self.total_shifts - self.remaining_shifts
        '''present = LabourHour.objects.all().filter(emp_id=self.emp_id,date__month=\
            11).count()
        
        obj = WorkingShift.objects.get(pk=1)#month=11,worksite=self.emp_id.work,category=self.emp_id.category)
        total = obj.working_days
        print(total,present)'''
        pps = Salary.objects.get(employee_name=self.emp_id).pay_per_shift
        print("PPS in deductions:",pps)
        deductions=self.leaves* pps
        print('deductions = ',deductions)
        return deductions
    
    @property
    def leaves(self):
        print("In leaves of Deductions")
        date = dt.date.today()
        mont = date.month  #previous month
        print('month ', mont)
        present = LabourHour.objects.all().filter(emp_id=self.emp_id,date__month=\
            mont).count()
        print(present)
        mont = dt.date.today().month
        year = dt.date.today().year
        m = month.Month(year,mont)
        print("month field m= ",m,"\nCategory ",self.emp_id.category)
        obj = WorkingShift.objects.get(worksite=self.emp_id.work.id,category=self.emp_id.category,month=m)# use pk=1 otherwise,month=11,worksite=self.emp_id.work,category=self.emp_id.category)
        print("obj ", obj)
        total = obj.working_days
        print("present n total ",present,total)
        return total - present
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f

class Overtime(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = MonthField(null=True)
    OT_shifts = models.IntegerField(default=0)
    #OT_pay = models.FloatField(default=0)

    def __str__(self):
<<<<<<< HEAD
        return str(self.emp_id.name)+str(self.month)
=======
        return str(self.emp_id.name)+ ' '+str(self.month)
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
    
    class Meta:
        unique_together=('emp_id','month')
    
    @property
    def OT_pay(self):
        #30 is hard coded must come from pay per shift
<<<<<<< HEAD
        return self.OT_shifts*30
=======
        pps = Salary.objects.get(employee_name=self.emp_id).pay_per_shift
        print("Hello",pps)
        return self.OT_shifts*pps
    
    @property
    def total_OT_shifts(self):
        print(self.month,self.month.month)
        ot=LabourHour.objects.filter(emp_id=self.emp_id,date__month=self.month.month)
        print("OT in Overtime monthly=", ot)
        total=0
        for o in ot:
            total+=o.overtime_shifts
        print("Total OT shifts", total)
        self.OT_shifts = total
        self.save()
        return total
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f

class Salary(models.Model):
    employee_name  = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False)
    base_sal = models.FloatField(default=0,blank=False)
    pay_per_shift = models.FloatField(default=0,blank=False)

<<<<<<< HEAD
    def __str__(self):
        return str(self.base_sal)
=======
   
    def getsalary(emp_id):
        sal = Salary.objects.get(employee_name=emp_id)
        return sal.base_sal

    def __str__(self):
        return str(self.employee_name.name)
    
    def getpps(emp_id):
        sal = Salary.objects.get(employee_name=emp_id)
        return sal.pay_per_shift
    
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
