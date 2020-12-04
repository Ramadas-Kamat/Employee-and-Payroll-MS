from django.db import models
#from employee.models import Employee

# Create your models here.
class Salary(models.Model):
    wages = models.FloatField()
    claims = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    #emp = models.OneToOneField(Employee,on_delete=models.CASCADE,null=True)
    
    @property
    def amount(self):
        return self.wages + self.claims + self.bonus
