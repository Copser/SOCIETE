import pytest
from django.test import TestCase

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

from landing_page.views import index, about


class MainPageTest(TestCase):
    """TODO: Test main page routing
    return: TODO
    """

    def test_root_resolvers_to_main_view(self):
        """TODO: test main page url routing
        retun: TODO
        """
        main_page = resolve('/')
        assert main_page.func

    def test_root_resolvers_to_about_view(self):
        """TODO: test about page url routing
        return: TODO
        """
        about_page = resolve('/about/')
        assert about_page.func

    def test_returns_appropriate_main_page_status_code(self):
        """TODO: test main page return proper status code
        return: TODO
        """
        index = self.client.get('/')
        assert index.status_code, 200

    def test_returns_appropriate_about_page_status_code(self):
        """TODO: test about page return proper status code
        return: TODO
        """
        about = self.client.get('/about')
        assert about.status_code, 200

    def test_if_index_html_template_is_returned(self):
        """TODO: test return if actual template is used
        return: TODO
        """
        index = self.client.get('/')
        assert index.content, \
                render_to_response("index.html").content

    def test_if_about_html_template_is_returned(self):
        """TODO: test return if actual template is used
        return: TODO
        """
        index = self.client.get('/about/')
        assert index.content, \
                render_to_response("about.html").content
