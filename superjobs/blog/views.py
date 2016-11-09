from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from .models import Post, Apply

# Create your views here.
def jobs(request):
    """TODO: create jobs view to list are current jobs
    return: TODO
    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/jobs.html')
    c = Context({'latest_posts': latest_posts, })
    return HttpResponse(t.render(c))
