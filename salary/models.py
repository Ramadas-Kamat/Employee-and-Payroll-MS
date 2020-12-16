from django.db import models
from employee.models import Employee

# Create your models here.
class Salary(models.Model):
    date = models.DateField(null=True)
    #wages = models.FloatField()
    claims = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.date) + str(self.emp.name)
    
    class Meta:
        unique_together = ('emp','date')
    @property
    def amount(self):
        return self.wages + self.claims + self.bonus

    def get_wage(self):
        return emp.base_sal
    
    def set_wage(self,wage):
        employee = self.emp
        employee.base_sal=wage
        employee.save()
