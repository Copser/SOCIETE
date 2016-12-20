# blog/tests/test_api.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Post


class PostTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(PostTests, cls).setUpClass()
        cls.superuser, created = User.objects.\
                get_or_create(
                    username="test-admin",
                )
        cls.superuser.is_active = True
        cls.superuser.is_superuser = True
        cls.superuser.save()

        cls.title = Post.objects.create(
            title="Job Testing Example"
        )
        cls.description = Post.objects.create(
            description="We are testing are job,"
            "description, for the job."
        )

    @classmethod
    def tearDownClass(cls):
        super(PostTests, cls).tearDownClass()
        cls.title.delete()
        cls.description.delete()
        cls.superuser.delete()

    def test_posts_list_api(self):
        url = resolve("/blog/posts/")
        data = {}
        response = self.client.get(url, data, format="json")
        assert response.status_code == 200
        assert response.data["count"] == Post.objects.count()
