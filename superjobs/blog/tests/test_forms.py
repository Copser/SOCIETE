from django.test import TestCase

# Create your tests here.
class FormTestMixin():
    """TODO: Create a mixin which will validate are form, we pass this into
    class of the form, name of the field expected to have and error, the
    expected error message, and the ata to initialize the form. This mixin
    will to appropriate validation and provide a helpful error message
    return: TODO
    """
    def assertFormError(self, form_cls,
                        expected_error_name,
                        expected_error_msg,
                        data):
        from pprint import pformat
        test_form = form_cls(data=data)

        # if we got and error the the form should not be valid
        self.assertFalse(test_form.is_valid())

        self.assertEqueals(
            test_form.errors[expected_error_name],
            expected_error_msg,
            msg="Expected {}: Actual {} : using data {}".format(
                test_form.errors[expected_error_name],
                expected_error_msg, pformat(data)
            )
        )
