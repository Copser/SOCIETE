# landing_page/tests/test_routing
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from landing_page.views import index, about, success

import pytest


def test_index_resolvers_to_main_page():
    main_page = resolve("/")
    assert main_page.func == index

def test_index_page_status_code(rf):
    request = rf.get('/')
    response = index(request)
    assert response.status_code == 200

def test_about_page_resolvers_to_about_page():
    about_page = resolve('/about/')
    assert about_page.func == about

def test_about_page_status_code(rf):
    request = rf.get('/about')
    response = about(request)
    assert response.status_code == 200

def test_success_page_resolvers_to_success_page():
    success_page = resolve("/success/")
    assert success_page.func == success

def test_success_page_status_code(rf):
    request = rf.get('/success')
    response = success(request)
    assert response.status_code == 200
