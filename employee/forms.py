from .models import *
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class WorksiteForm(ModelForm):
    class Meta:
        model=Worksite
        exclude = ()
        help_texts = {
            'name':_("Enter name here"),
            'contact':_("Enter number starting with country code"),
            'location':_('Where is the site located?')
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['base_sal']
        labels = {
            'lname':_('Lastname'),
            'doj':_('Date of Joining'),
            'work':_('Worksite'),
        }
        help_texts = {
            'username':_("Select a username"),
            'contact':_("Enter number starting with country code"),
            
        }

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        exclude=()
        help_texts = {
            'in_time':_("Enter time of entry"),
            'out_time':_("Enter time of exit"),
        }

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        exclude=('num_of_emp',)
        help_texts = {
            'name':_("Enter name of Employee Category"),
        }
    '''def clean_fields(self):
        pattern = r'[^A-Za-z]'
        try:
            if re.findall(pattern,self.name) != [] :
                raise ValidationError({'name':_("Invalid name provided")})
        except:
            pass'''
