from django.test import TestCase
from django.core.urlresolvers import resolve
from views import index


# Create your tests here.
class HomePageTest(TestCase):

    """Docstring for HomePageTest. Testing are landing page localy. """

    def test_root_url_resolves_to_home_page_view(self):
        """TODO: to be defined1. """
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_returns_appropriate_html(self):
        """TODO: Docstring for test_returns_appropriate_pagr.
        :returns: TODO

        """
        index = self.client.get('/')
        self.assertEqual(index.status_code, 200)
