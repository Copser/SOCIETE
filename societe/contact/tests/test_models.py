from django.test import TestCase, SimpleTestCase
from ..forms import ContactView
from ..models import ContactForm
from datetime import datetime, timedelta


class UserModelTest(TestCase):

    """Docstring for UserModelTest. Initializing test for the contact
        application.
    """
    @classmethod
    def setUpTestData(cls):
        """TODO: define test data for contact application."""
        ContactForm(first_name='sarah', last_name='doe', email='sarahdoe@email.com').save()
        ContactForm(first_name='john', last_name='doe', email='johdoe@email.com').save()
        cls.firstUser = ContactForm(
            email='petarp@email.com',
            first_name='petar',
            last_name='popovic',
            timestamp=datetime.today() + timedelta(days=2)
        )
        cls.firstUser.save()

    def test_contactform_str_return_email(self):
        """TODO: Docstring for test_contactform_str_return_email.
        :returns: return user email address

        """
        self.assertEqual('petarp@email.com', str(self.firstUser))

    def test_contactform_str_return_first_name(self):
        """TODO: Docstring for test_contactform_str_return_first_name.

        :arg1: TODO
        :returns: return first_name

        """
        self.assertEqual('petar', str(self.firstUser))

    def test_ordering(self):
        """TODO: Docstring for test_ordering.
        :returns: TODO

        """
        contacts = ContactForm.objects.all()
        self.assertEqual(self.firstUser, contacts[0])


class ContactViewTest(SimpleTestCase):

    """Docstring for ContactViewTest. define what fields we have inside form."""
    def test_display_fields(self):
        """TODO: to be defined1. """
        expected_fields = ['first_name', 'last_name', 'email', 'mobile',
                           'birthday', 'move_in_date', 'move_out_date',
                           'country', 'message']
        self.assertEqual(ContactView.Meta.fields, expected_fields)
