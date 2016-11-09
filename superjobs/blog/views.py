from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from .models import Post, Apply

# Create your views here.
def jobs(request):
    """TODO: create jobs view to list are current jobs
    return: TODO
    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template(
        'blog/jobs.html'
    )
    c = Context({
        'latest_posts': latest_posts,
    })
    return HttpResponse(
        t.render(c)
    )


def post(request, post_id):
    """TODO: creating post so we can sort out are jobs list
    return: TODO
    """
    single_post = get_object_or_404(
        Post,
        pk=post_id
    )
    t = loader.get_template(
        'blog/post.html'
    )
    c = Context({
        'single_post': single_post,
    })
    return HttpResponse(
        t.render(c)
    )
