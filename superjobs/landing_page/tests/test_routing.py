# landing_page/tests/test_routing
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import pytest


from landing_page.views import index, about, success

def test_index_page_status_code(rf):
    request = rf.get('/')
    response = index(request)
    assert response.status_code == 200

def test_about_page_status_code(rf):
    request = rf.get('/about')
    response = about(request)
    assert response.status_code == 200

def test_success_page_status_code(rf):
    request = rf.get('/success')
    response = success(request)
    assert response.status_code == 200
