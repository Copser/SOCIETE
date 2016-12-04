import pytest
from django import forms

from blog.forms import ApplyForm

def test_apply_to_form_data_validation_for_invalid_data(self):
    """TODO: testing data validation in ApplyForm
    return: TODO
    """
    form = ApplyForm(
        {
            'full_name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'mobile': '',
            'birthdate': '10.14.1984',
            'previous_company_name': 'Company Name',
            'previous_company_email': 'company@example.com',
            'previous_job_title': 'mad hatter',
            'jobs_experience': 'I have it',
            'hospitality_relations_experience': 'I have this to',
            'working_hours': '200',
            'choose_desired_working_hours_wage': '10$',
            'type_of_driver_licences': 'A'}
    )

    assert form.is_valid() == True

