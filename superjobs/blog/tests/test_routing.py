# blog/tests/test_routing.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs, posts_list, posts_detail, apply_to

import pytest


<<<<<<< HEAD
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

<<<<<<< HEAD
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
        assert jobs_page_status_code.status_code == 302

    def test_posts_list_api_return_proper_status_code(self):
        """TODO: test posts_list api status code, should return 200
        status_code if page exists
        return: TODO
        """
        posts_lists_status_code = self.client.get('/blog/posts/')
        assert posts_lists_status_code.status_code == 200
=======
>>>>>>> rest_framework_development_branch

    def test_apply_to_return_proper_status_code(self):
        """TODO: test apply_to status code return 200
        return: TODO
        """
        apply_to_status_code = self.client.get('/blog/apply_to/')
        assert apply_to_status_code.status_code == 200
=======
def test_jobs_resolvers_to_blog_jobs():
    jobs_page = resolve("/blog/jobs/")
    assert jobs_page.func == jobs

def test_blog_jobs_returns_appropriate_html(client):
    jobs = client.get("/blog/jobs/")
    assert jobs.status_code == 302, "Tests will it redirect to login_url"

def test_apply_to_resolvers_to_blog_apply_to():
    blog_apply_to = resolve('/blog/apply_to/')
    assert blog_apply_to.func == apply_to

def test_blog_apply_to_returns_appropriate_html(client):
    apply_to = client.get("/blog/apply_to/")
    assert apply_to.status_code == 302, "Tests will it redirect to login_url"
>>>>>>> rest_framework_development_branch
