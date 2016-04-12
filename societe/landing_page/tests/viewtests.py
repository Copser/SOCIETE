from django.test import TestCase
from django.core.urlresolvers import resolve
from ..views import index
from django.test import RequestFactory


# Create your tests here.
class HomePageTest(TestCase):

    """Docstring for HomePageTest. Testing are landing page localy. """
    # Setup
    def setUpClass(cls):
        """TODO: Docstring for setUpClass.
        :returns: TODO

        """
        super(HomePageTest, cls).setUpClass()
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}

    def test_root_url_resolves_to_home_page_view(self):
        """TODO: to be defined1. """
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_response_code(self):
        """TODO: Docstring for test_returns_appropriate_pagr.
        :returns: TODO

        """
        resp = index(self.request)
        self.assertEqual(resp.status_code, 200)
