# blog/api/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from blog.models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    """TODO: Define api list view for the Post model,
    using rest_framework generics.ListAPIView
    return: TODO
    """
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    """TODO: Define api detailed view for the Post model,
    using rest_framework generics.RetrieveAPIView
    return: TODO
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
