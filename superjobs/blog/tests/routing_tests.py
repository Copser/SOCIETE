import pytest
from django.test import TestCase

from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs, post, posts_list, posts_detail, \
        apply_to, success

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
        assert jobs_page.func

    def test_post_resolvers_to_post_view(self):
        """TODO: testing post views routung, shold return post url
        return: TODO
        """
        post_page = resolve('/blog/post/')
        assert post_page.func

    def test_post_list_resolvers_to_post_list_api_view(self):
        """TODO: testing posts_list url routing, should return posts_list
        return: TODO
        """
        post_list_jobs_api = resolve('/blog/posts/')
        assert post_list_jobs_api.func

    def test_post_detail_resolvers_to_post_deatail_api_view(self):
        """TODO: testing posts_detail url api routing, should return posts_detail
        return: TODO
        """
        posts_detail_jobs_api = resolve('/blog/posts/1/')
        assert posts_detail_jobs_api.func

    def test_apply_to_resolvers_to_apply_to_view(self):
        """TODO: testing apply_to views url routing, should return apply_to url
        return: TODO
        """
        apply_to_page_url = resolve('blog/apply_to')
        assert apply_to_page_url.func
