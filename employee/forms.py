from .models import *
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class WorksiteForm(ModelForm):
    class Meta:
        model=Worksite
        exclude = ()
        help_texts = {
            'name':_("Enter name here"),
        }

        