from django import forms
from django.forms import ModelForm, extras

from .models import ApplySuperForm
import datetime


class ApplySuperView(ModelForm):
    """
    TODO: Create class which will represent a form for are User to appy

    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1939, 2010)))
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'telephone', 'mobile',
                  'birthdate', 'experience', 'references', 'hourly_rate',
                  'licences']
        model = ApplySuperForm
