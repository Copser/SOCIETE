# landing_page/tests/test_routing
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from landing_page.views import index, about, success

import pytest


class MainPageTests(TestCase):
    """TODO: Testing main page, about page, and success page
    ruting, status_code
    return: TODO
    """
    def test_index_resolvers_to_main_page(self):
        main_page = resolve("/")
        assert main_page.func == index

    def test_index_page_status_code(self):
        index = self.client.get('/')
        assert index.status_code == 200

    def test_about_page_resolvers_to_about_page(self):
        about_page = resolve('/about/')
        assert about_page.func == about

    def test_about_page_status_code(self):
        about = self.client.get('/about/')
        assert about.status_code == 200

    def test_success_page_resolvers_to_success_page(self):
        success_page = resolve("/success/")
        assert success_page.func == success

    def test_success_page_status_code(self):
        success = self.client.get('/success/')
        assert success.status_code == 200
