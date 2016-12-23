# blog/api/serializers.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """TODO: Providing serialization for blog Post
    model instance
    return: TODO
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'created_at', 'tag', 'slug')
