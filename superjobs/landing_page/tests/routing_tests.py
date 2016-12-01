import pytest
from django.test import TestCase

from django.core.urlresolvers import resolve

from landing_page.views import index, about


class MainPageTest(TestCase):
    """TODO: Test main page routing
    return: TODO
    """

    def test_root_resolvers_to_main_view(self):
        main_page = resolve('/')
        assert main_page.func, index

    def test_root_resolvers_to_about_view(self):
        about_page = resolve('/about/')
        assert about_page.func, about
