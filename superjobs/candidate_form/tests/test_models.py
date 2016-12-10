# candidate_form/tests/test_models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from candidate_form.models import CandindateFormModel

import pytest



@pytest.mark.django_db
def test_candidate_form_models_field():
    candidate_info = CandindateFormModel(
        #
        # Personal Information
        #
        first_name="John",
        last_name="Doe",
        email="johndoe@gmail.com",
        mobile_phone_number="3876543434343",
        city="New York",
        street_address="Broadway",
        #
        # Experience Information
        #
        candidate_skill="Housekeep",
        candidate_experience="One Year +",
        candidate_hospitality_experience="Two Year",
        candidate_training="Self Taught",
        #
        # Additional Information
        # 
        work_hours="30+",
        payed_per_hour="20.0",
        valid_work_permit="Yes",
        drivers_license="C"
    )
    candidate_info.save()
    #
    # Personal Information
    #
    assert candidate_info.first_name == "John"
    assert candidate_info.last_name == "Doe"
    assert candidate_info.email == "johndoe@gmail.com"
    assert candidate_info.mobile_phone_number == "3876543434343"
    assert candidate_info.city == "New York"
    assert candidate_info.street_address == "Broadway"
    #
    # Experience Information
    # 
    assert candidate_info.candidate_skill == "Housekeep"
    assert candidate_info.candidate_experience == "One Year +"
    assert candidate_info.candidate_hospitality_experience == "Two Year"
    assert candidate_info.candidate_training == "Self Taught"
    #
    # Additional Information
    #
    assert candidate_info.work_hours == "30+"
    assert candidate_info.payed_per_hour == "20.0"
    assert candidate_info.valid_work_permit == "No"
    assert candidate_info.drivers_license == "B"
