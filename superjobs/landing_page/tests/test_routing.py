import pytest
from django.test import TestCase

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

from landing_page.views import index, about, success


def test_index_page_status_code(rf):
    request = rf.get('/')
    response = index(request)
    assert response.status_code == 200

def test_about_page_statis_code(rf):
    request = rf.get('/about')
    response = about(request)
    assert response.status_code == 200
