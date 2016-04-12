from django.test import TestCase
from ..models import ContactForm
from django.utils import timezone
from django.core.urlresolvers import reverse


# Model test
class ContactFormTest(TestCase):
    """Docstring for ContactFormTest. Building test for contact/models.py """
    def create_contactform(self, first_name="tester", email="test@testing.com"):
        """creating first_name and email for ContactFormTest"""
        return ContactForm.objects.create(first_name=first_name, email=email,
                                          timestamp=timezone.now())

    def test_contactform_creation(self):
        """TODO: Docstring for test_contactform_creation.
        testing to see will first_name and email be created_at
        :returns: TODO

        """
        w = self.create_contactform()
        self.assertTrue(isinstance(w, ContactForm))
        self.assertEqual(w.__unicode__(), w.email)
