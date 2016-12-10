# blog/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from .models import Post, Apply
from .serialziers import PostSerializer
from .forms import ApplyForm


# helper function
def get_popular_posts():
    popular_posts = Post.objects.order_by('-views')[:5]
    return popular_posts

# Create your views here.
# @login_required(login_url='/accounts/signup')
def jobs(request):
    """TODO: create jobs view to list are current jobs,
    polish are urls so it can be more human readable,
    slug field added
    return: TODO
    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/jobs.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    """TODO: creating post so we can sort out are jobs list,
    slug field added
    return: TODO
    """
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1
    single_post.save()
    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


@api_view(['GET', 'POST'])
def posts_list(request, format=None):
    """TODO: List all jobs, or create new jobs
    return: TODO
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk, format=None):
    """TODO: Retreive, update, delete post instance
    return: TODO
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Use Generic class-based views to represent are user
#class UserList(generics.ListAPIView):
#    """TODO: create read-only view for user representation,
#    associationg posts with user by adding perform_create
#    method
#    Add permissions class IsAuthenticatedOrReadOnly so we can
#    restrict who owners, if owner is authenticated he will have
#    read-write access, if not he will only have read-only access
#    return: TODO
#    """
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)
#
#
#class UserDetail(generics.RetrieveAPIView):
#    """TODO: create read-only view for user representation
#    Add permissions class IsAuthenticatedOrReadOnly so we can
#    restrict who owners, if owner is authenticated he will have
#    read-write access, if not he will only have read-only access
#    return: TODO
#    """
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def apply_to(request):
    """TODO: apply view will render ApplyForm,
    we are using django-bootstrap3 to style are form,
    and it will suport file upload for
    return: TODO
    """
    if request.method == 'POST':
        form = Apply(request.POST)
        if form.is_valid():
            apply_form = form.save(commit=False)
            apply_form.save()
            messages.add_message(
                request, messages.INFO, "You have successfully applied for\
                this ongoin position. Thanks you."
            )
            return HttpResponseRedirect('/success')
        else:
            print(form.errors)
    else:
        form = ApplyForm()
    t = loader.get_template('blog/apply_to.html')
    c = RequestContext(
        request,
        {
            'form': form,
        }
    )
    return HttpResponse(t.render(c))


def success(request):
    """TODO: create success views,
    we will display useful information for new jobs applicants
    return: TODO
    """
    return render_to_response(
        'blog/success.html',
        context_instance=RequestContext(request)
    )
