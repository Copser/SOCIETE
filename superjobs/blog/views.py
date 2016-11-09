from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from .models import Post, Apply

# Create your views here.
def jobs(request):
    """TODO: create jobs view to list are current jobs, polish are urls so it can be more human readable,
    I'm creating and using for loop to replace spaces in post name with underscores, so title will be seen
    with underscores
    return: TODO
    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template(
        'blog/jobs.html'
    )
    context_dict = {
        'latest_posts': latest_posts,
    }
    for post in latest_posts:
        post.url = post.title.replace(' ', '_')
    c = Context(
        context_dict
    )
    return HttpResponse(
        t.render(c)
    )


def post(request, post_id):
    """TODO: creating post so we can sort out are jobs list, update post so it will suport underscore jobs
    searching
    return: TODO
    """
    single_post = get_object_or_404(
        Post,
        title=post_url.replace('_', ' ')
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
