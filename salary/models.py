from django.db import models
from employee.models import Employee

# Create your models here.
class Salary(models.Model):
    date = models.DateField(null=True)
    wages = models.FloatField()
    claims = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    
    class Meta:
        unique_together = ('emp','date')
    @property
    def amount(self):
        return self.wages + self.claims + self.bonus
