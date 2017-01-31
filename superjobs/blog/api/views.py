# blog/api/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .permissions import IsApplied

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


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """TODO: Define viewsets for Post, we will have better
    inrecation in our API and we let REST build the URLs dynamically
    return: TODO
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
