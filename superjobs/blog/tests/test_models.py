# blog/tests/test_models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import pytest

from blog.models import Post, ApplyFormModel


pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test_jobs_post_field_create():
    """TODO: testing post field, will be create correctly
    return: TODO
    """
    post_jobs = Post(title="TestJob",
                     description="We need you!",
                     tag="plumbing, housekeep",
                     slug="test-job")
    post_jobs.save()
    assert post_jobs.title == "TestJob"
    assert post_jobs.description == "We need you!"
    assert post_jobs.tag == "plumbing, housekeep"
    assert post_jobs.slug == "testjob"

def test_post_str_method_return_self_title():
    """TODO: testing will __str__ method return title
    return: TODO
    """
    post_string_method = Post(title="My Job Title")
    assert str(post_string_method) == post_string_method.title


@pytest.mark.django_db
def test_apply_models_custom_fields():
    """TODO: test apply model method fields
    return: TODO
    """
    apply_method = ApplyFormModel(

        # Personal Information
        first_name = "John",
        last_name = "Doe",
        email = "johndoe@example.com",
        mobile_phone = "+11223344556677",
        confirm_mobile_phone = "+11223344556677",
        city = "Queens",
        street_address = "",

        # Experience Information
        candidate_skill = "Plumbing",
        candidate_experience = "Two Years",
        candidate_hospitality_experience = "One Year",
        candidate_training = "Other",

        # Other Information
        work_hours = "20+",
        payed_per_hour = "20.00",
        valid_work_permit = "Yes",
        drivers_license = "A"
    )

    # Personal Information
    assert apply_method.first_name == "John"
    assert apply_method.last_name == "Doe"
    assert apply_method.email == "johndoe@example.com"
    assert apply_method.mobile_phone == "+11223344556677"
    assert apply_method.confirm_mobile_phone == "+11223344556677"
    assert apply_method.city == "Queens"
    assert apply_method.street_address == ""

    # Experience Information
    assert apply_method.candidate_skill == "Plumbing"
    assert apply_method.candidate_experience == "Two Years"
    assert apply_method.candidate_hospitality_experience == "One Year"
    assert apply_method.candidate_training == "Other"

    # Other Information
    assert apply_method.work_hours == "20+"
    assert apply_method.payed_per_hour == "20.00"
    assert apply_method.valid_work_permit == "Yes"
    assert apply_method.drivers_license == "A"

def test_apply_str_method_return_self_title():
    """TODO: testing will __str__ method return title
    return: TODO
    """
    apply_string_method = ApplyFormModel(email="email@email.com")
    assert str(apply_string_method) == apply_string_method.email
