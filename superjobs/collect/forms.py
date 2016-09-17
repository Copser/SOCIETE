from django import forms
from django.forms import ModelForm, extras

from .models import ApplySuperForm
import datetime


class ApplySuperView(ModelForm):
    """
    TODO: Create class which will represent a form for are User to appy

    """
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'telephone', 'mobile',
                  'birthday', 'experience', 'references', 'hourly_rate',
                  'licences']
        model = ApplySuperForm
