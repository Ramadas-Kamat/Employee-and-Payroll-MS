from django.forms import ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class PayrollForm(ModelForm):
    claims = forms.FloatField(min_value = 0,max_value=1000,help_text='Limit is 1000')
    bonus = forms.FloatField(min_value=0,max_value=2000,help_text='Limit is 2000')
    class Meta:
        model = Payroll
        exclude=('wages',)
        labels={
        'OT':_("Overtime"),
        'emp':_("Employee"),
        }
        error_messages={
            'claims':{
                'min_value':_("Value cannot be negative"),
            }
        }
    

    