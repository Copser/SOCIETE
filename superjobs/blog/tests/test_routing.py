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
    def test_jobs_resolvers_to_jobs_view(self):
        """TODO: should return jobs page
        return: TODO
        """
        jobs_page = resolve('/blog/jobs/')
        jobs_page_status_code = self.client.get('/blog/jobs/')
        assert jobs_page.func == jobs
        assert jobs_page_status_code.status_code == 200

    def test_post_list_resolvers_to_post_list_api_view(self):
        """TODO: testing posts_list url routing, should return posts_list
        return: TODO
        """
        posts_list_jobs_api = resolve('/blog/posts/')
        posts_lists_status_code = self.client.get('/blog/posts/')
        assert posts_list_jobs_api.func == posts_list
        assert posts_lists_status_code.status_code == 200

    def test_post_detail_resolvers_to_post_deatail_api_view(self):
        """TODO: testing posts_detail url api routing, should return posts_detail
        return: TODO
        """
        posts_detail_api = resolve('/blog/posts/1/')
        assert posts_detail_api.func == posts_detail


    def test_apply_to_return_proper_status_code(self):
        """TODO: test apply_to status code return 200
        return: TODO
        """
        apply_to_status_code = self.client.get('/blog/apply_to/')
        assert apply_to_status_code.status_code == 200
