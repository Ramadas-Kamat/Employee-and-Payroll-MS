from django.contrib import admin
from .models import *
<<<<<<< HEAD
=======
from .forms import *
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
# Register your models here.
#admin.site.register(Overtime, Deduction)
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("empname", "date",'claims','bonus')

    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'

@admin.register(Overtime)
class OvertimeAdmin(admin.ModelAdmin):
    list_display = ("empname", "month",'OT_shifts','OT_pay')

    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'

@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    list_display = ("empname", "month")

=======
    form=PayrollForm
    list_display = ("empname", "date",'wages','claims','bonus','payable')
    exclude = ('wages',)
    def empname(self,obj):
        return obj.emp.name
    empname.short_description = 'Employee name'

    def payable(self,obj):
        return obj.amount
    
    payable.short_description = "Payable Amount"

    
    

@admin.register(Overtime)
class OvertimeAdmin(admin.ModelAdmin):
    list_display = ("empname", "month",'total_OT_shifts','OT_pay')
    exclude = ('OT_shifts',)
    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'
    
    

@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    list_display = ("empname", "month",'leaves','total_deductions')
    exclude = ('remaining_shifts',)
>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'

<<<<<<< HEAD
=======
    #exclude=('remaining_shifts',)

>>>>>>> 2cef9e94d72fb1967f5535729c7c8f1b94f4cb6f
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("empname", "base_sal",'pay_per_shift')

    def empname(self,obj):
        return obj.employee_name.name
    empname.short_description = 'Employee name'