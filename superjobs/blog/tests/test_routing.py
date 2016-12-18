# blog/tests/test_routing.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs, posts_list, posts_detail, apply_to

import pytest


class JobsPageTest(TestCase):
    """TODO: testing blog/ routing, we want to see if are pages are
    wired correctly
    return: TODO
    """

    def test_jobs_resolvers_to_blog_jobs(self):
        jobs_page = resolve('/blog/jobs/')
        assert jobs_page.func == jobs

    def test_apply_to_resolvers_to_blog_apply_to(self):
        blog_apply_to = resolve('/blog/apply_to/')
        assert blog_apply_to.func == apply_to

    def test_blog_posts_resolvers_to_blog_posts_api(self):
        blog_posts = resolve('/blog/posts/')
        assert blog_posts.func == posts_list
