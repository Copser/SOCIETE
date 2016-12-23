# blog/api/permissions.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import BasePermission


class IsApplied(BasePermission):
    """TODO: subclassing has_object_permission() to check that
    the user performing the request is present in the user relationship
    of the Post model, we are going to use this in new Post serializing
    content
    return: TODO
    """
    def has_object_permission(self, request, view, obj):
        return obj.user.filter(id=request.user.id).exists()
