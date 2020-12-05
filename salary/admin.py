from django.contrib import admin
from .models import Salary
# Register your models here.
#admin.site.register(Salary)
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("emp", "date",'claims','bonus')