# blog/tests/test_routing.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.test import TestCase

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs, post, posts_list, posts_detail, \
        apply_to, success

import pytest


@python_2_unicode_compatible
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
        assert jobs_page.func == jobs

    def test_post_resolvers_to_post_view(self):
        """TODO: testing post views routung, shold return post url
        return: TODO
        """
        post_page = resolve('/blog/post/')
        assert post_page.func == post

    def test_post_list_resolvers_to_post_list_api_view(self):
        """TODO: testing posts_list url routing, should return posts_list
        return: TODO
        """
        posts_list_jobs_api = resolve('/blog/posts/')
        assert posts_list_jobs_api.func == posts_list

    def test_post_detail_resolvers_to_post_deatail_api_view(self):
        """TODO: testing posts_detail url api routing, should return posts_detail
        return: TODO
        """
        posts_detail_jobs_api = resolve('/blog/posts/1/')
        assert posts_detail_jobs_api.func == posts_detail

    def test_apply_to_resolvers_to_apply_to_view(self):
        """TODO: testing apply_to views url routing, should return apply_to url
        return: TODO
        """
        apply_to_page_url = resolve('/blog/apply_to/')
        assert apply_to_page_url.func == apply_to

    def test_success_to_resolve_to_success_url_views(self):
        """TODO: testing success views url routung, should return success url
        return: TODO
        """
        success_page_url = resolve('/blog/success/')
        assert success_page_url.func == success

    def test_return_appropriate_post_page_status_code(self):
        """TODO: test post page status code
        return: TODO
        """
        post_page_status_code = self.client.get('/blog/post/')
        assert post_page_status_code.status_code == 404

    def test_return_appropriate_jobs_page_status_code(self):
        """TODO: test jobs page status code
        return: TODO
        """
        jobs_page_status_code = self.client.get('/blog/jobs/')
        assert jobs_page_status_code.status_code == 200

    def test_posts_list_api_return_proper_status_code(self):
        """TODO: test posts_list api status code, should return 200
        status_code if page exists
        return: TODO
        """
        posts_lists_status_code = self.client.get('/blog/posts/')
        assert posts_lists_status_code.status_code == 200

    def test_apply_to_return_proper_status_code(self):
        """TODO: test apply_to status code return 200
        return: TODO
        """
        apply_to_status_code = self.client.get('/blog/apply_to/')
        assert apply_to_status_code.status_code == 200

    def test_success_return_proper_status_code(self):
        """TODO: test success status code return 200
        return: TODO
        """
        success_status_code = self.client.get('/blog/success/')
        assert success_status_code.status_code == 200
