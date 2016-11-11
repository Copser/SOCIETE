from django import forms
from django.forms import extras

from .models import Apply


class ApplyForm(forms.ModelForm):
    """TODO: Create apply form so are applicants can apply to jobs
    return: TOOD
    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1975, 2010)))
    class Meta:
        model = Apply
        fields = ['full_name', 'email', 'mobile', 'birthdate',
                  'previous_company_name', 'previous_company_email', 'previous_job_title',
                  'jobs_experience', 'hospitality_relations_experience',
                  'working_hours', 'choose_desired_working_hours_wage',
                  'type_of_driver_licences', 'applicants_cv']
        widgets = {
            'choose_desired_working_hours_wage': forms.NumberInput(attrs= {'min': '0', 'max': '35', 'step': '1'}),
        }
