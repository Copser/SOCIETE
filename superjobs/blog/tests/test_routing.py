# blog/tests/test_routing.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs, posts_list, posts_detail, apply_to

import pytest

@pytest.mark.django_db
class BlogTests(TestCase):
    def test_jobs_resolvers_to_blog_jobs(self):
        jobs_page = resolve("/blog/jobs/")
        assert jobs_page.func == jobs

    def test_blog_jobs_returns_appropriate_html(self):
        jobs = self.client.get("/blog/jobs/")
        assert jobs.status_code == 302, "Tests will it redirect to login_url"

    def test_apply_to_resolvers_to_blog_apply_to(self):
        blog_apply_to = resolve('/blog/apply_to/')
        assert blog_apply_to.func == apply_to

    def test_blog_apply_to_returns_appropriate_html(self):
        apply_to = self.client.get("/blog/apply_to/")
        assert apply_to.status_code == 302, "Tests will it redirect to login_url"
