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
            'lname':_('Last name'),
            'doj':_('Date of Joining'),
            'work':_('Worksite'),
        }
        help_texts = {
            'username':_("Select a username"),
            'contact':_("Enter number starting with country code"),
            
        }
    def clean_fields(self,exclude=None):
        print("Hi in clean method of form")
        pattern = r'[^A-Za-z]'
        flag1=flag2=False
        try:
            if re.findall(pattern,self.name) != [] :
                
                flag1=True
                raise ValidationError({'name':_('Incorrect name')})
            if re.findall(pattern,self.lname) != [] :
                
                flag2=True
                raise ValidationError({'lname':_('Incorrect lastname')})
            
            if flag1 and flag2:
                raise ValidationError({
            'name':ValidationError(_("Incorrect first name")),
            'lname':ValidationError(_("Incorrect last name"))
            })
        except:
            pass

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
