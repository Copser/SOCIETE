# blog/tests/test_forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest
import pytest

from blog.forms import ApplyForm


class FormTesterMixin():
    """TODO: Help us validate are form, pass in the class of the form,
    the name of the field expected to have an error, the expected error
    message (you can add this with pytest), and the data to initialize
    the form.
    FormTesterMixin will do all appropriate validation and provide a
    helpful error message that will tell us the failure and what
    data triggered the failure.
    return: TODO
    """
    def assertFormError(self, form_cls, excepted_error_name,
                        excepted_error_msg, data):

        from pprint import pformat
        test_form = form_cls(data=data)

        self.assertEquals(
            test_form.errors[excepted_error_name],
            excepted_error_msg,
            msg="Expected {}: Actual {}: using data {}".format(
                test_form.errors[excepted_error_name],
                excepted_error_msg, pformat(data)
            )
        )


class TestFormCase(unittest.TestCase, FormTesterMixin):
    """TODO: Constructing series of ApplyForm test about form validation
    and field validation
    return: TODO
    """
    def test_apply_to_form_data_validation_for_invalid_data(self):
        """TODO: testing data validation in ApplyForm
        return: TODO
        """
        invalid_data_list = [
            {'data': {'first_name': 'John'},
             'error': ('last_name', [u'This field is required.'])},
            {'data': {'last_name': 'Doe'},
             'error': ('first_name', [u'This field is required.'])},
        ]

        for invalid_data in invalid_data_list:
            self.assertFormError(ApplyForm, invalid_data['error'][0],
                   invalid_data['error'][1],
                   invalid_data["data"])
