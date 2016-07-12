from django.test import TestCase

from .models import User
from .forms import CardForm

import unittest

# Create your tests here.


class UserModelTest(TestCase):

    """Docstring for UserModelTest. """
    @classmethod
    def setUpClass(cls):
        """TODO: Docstring for setUpClass.
        :returns: TODO

        """
        cls.test_user = User(email="testUser@test.com", name="Test", last_name="User")
        cls.test_user.save()

    def test_user_to_string_print_email(self):
        """TODO: to be defined1. """
        self.assertEqual(str(self.test_user), "testUser@test.com")

    def test_get_by_id(self):
        """TODO: Docstring for test_get_by_id.
        :returns: TODO

        """
        self.assertEqual(User.get_by_id(1), self.test_user)

    @classmethod
    def tearDownClass(cls):
        """TODO: Docstring for tearDownClass.
        :returns: TODO

        """
        cls.test_user.delete()


class FormTesterMixin():

    """Docstring for FormTesterMixin. This function will do all appropriate validation and provide a
    helpful error message that not only tells you the failure - but what data triggered the failure
    """

    def assertFormError(self, form_cls, expected_error_name,
                        expected_error_msg, data):
        """TODO: to be defined1. """
        from pprint import pformat
        test_form = form_cls(data=data)

        # if we get an error then the form should not be valid
        self.assertFalse(test_form.is_valid())

        self.assertEqual(
            test_form.errors[expected_error_name],
            expected_error_msg,
            msg="Expected{} : Actual{} : using data {}".format(
                test_form.errors[expected_error_name],
                expected_error_msg, pformat(data)
            )
        )


class FormTest(unittest.TestCase, FormTesterMixin):

    """Docstring for FormTest. """

    def test_card_form_data_validation_for_invalid_data(self):
        """TODO: to be defined1. """
        invalid_data_list = [
            {'data': {'email': 'j@j.com'},
                'error': ('last_name', [u'This field is required.'])},
            {'data': {'last_name': 'j'},
                'error': ('email', [u'This field is required.'])}
        ]

        for invalid_data in invalid_data_list:
            self.assertFormError(CardForm,
                                 invalid_data['error'][0],
                                 invalid_data['error'][1],
                                 invalid_data['data'])
