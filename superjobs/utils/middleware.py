# utils/middleware.py
# -*- coding: UTF-8 -*-
from threading import local
_thread_locals = local()

def get_current_request():
    """TODO: Returns the HttpRequest object for this thread
    return: TODO
    """
    return getattr(_thread_locals, "request", None)

def get_current_user():
    """TODO: returns the current user if it exists or None otherwise
    return: TODO
    """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)

class ThreadLocalMiddleware(object):
    """TODO: Middleware that adds the HttpRequest object
        to thread local storage
    return: TODO
    """
    def process_request(self, request):
        _thread_locals.request = request
