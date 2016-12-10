# candidate_form/tests/test_models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from candidate_form.models import CandindateFormModel

import pytest



@pytest.mark.django_db
def test_personal_information_models_fields():
    personal_info = CandindateFormModel(
        first_name="John",
        last_name="Doe",
        email="johndoe@gmail.com",
        mobile_phone_number="3876543434343",
        city="New York",
        street_address="Broadway"
    )
    personal_info.save()

    assert personal_info.first_name == "John"
    assert personal_info.last_name == "Doe"
    assert personal_info.email == "johndoe@gmail.com"
    assert personal_info.mobile_phone_number == "3876543434343"
    assert personal_info.city == "New York"
    assert street_address == "Broadway"
