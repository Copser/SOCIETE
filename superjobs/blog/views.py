# blog/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Post, ApplyFormModel
from .forms import ApplyForm


# helper function
def get_popular_posts():
    popular_posts = Post.objects.order_by("-views")[:5]
    return popular_posts

# Create your views here.
# @login_required(login_url='/accounts/login')
def jobs(request):
    """TODO: create jobs view to list are current jobs,
    polish are urls so it can be more human readable,
    slug field added
    return: TODO
    """
    latest_posts = Post.objects.all().order_by("-created_at")
    t = loader.get_template("blog/jobs.html")
    context_dict = {
        "latest_posts": latest_posts,
        "popular_posts": get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


# @login_required(login_url='/accounts/login')
def post(request, slug):
    """TODO: creating post so we can sort out are jobs list,
    slug field added
    return: TODO
    """
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1
    single_post.save()
    t = loader.get_template("blog/post.html")
    context_dict = {
        "single_post": single_post,
        "popular_posts": get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


# @login_required(login_url='/accounts/login')
def apply_to(request):
    """TODO: ApplyForm validation logic
    request: TODO
    """
    if request.method == "POST":
        form = ApplyForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect("/success")
    else:
        form = ApplyForm()

    return render_to_response(
        "blog/apply_to.html",
        context_instance=RequestContext(
            request,
            {"form": form},
        )
    )
