from django import forms
from django.forms import ModelForm, extras

from .models import ApplyForm
import datetime


class ApplyFormView(ModelForm):
    """TODO: representing labor form
    return: TODO
    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1987, 2010)))
    class Meta:
        model = ApplyForm
        fields = ['full_name', 'email', 'mobile', 'hourly_rate', 'working_hours',
                  'drivers_license', 'curriculum_vitae']
