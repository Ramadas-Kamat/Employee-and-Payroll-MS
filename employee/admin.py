from django.contrib import admin
from .models import Employee, Attendance , Worksite
#from .models2 import Worksite
# Register your models here.
#admin.site.register((Attendance, Worksite))

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name",'doj')

@admin.register(Worksite)
class WorksiteAdmin(admin.ModelAdmin):
    list_display = ( "name",'location','man_name')
    def man_name(self,obj):
        man = obj.manager

        return man.name
    man_name.short_description = "Manager"

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("date", "emp_name",'in_time','out_time')

    def emp_name(self,obj):
        emp = obj.emp_id

        return emp.name
    emp_name.short_description = "Name"
