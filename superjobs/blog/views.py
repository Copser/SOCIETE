from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Apply
from .forms import ApplyForm


# helper function
def popular_posts():
    popular_posts = Post.objects.order_by('-views')[:5]
    return popular_posts

# Create your views here.
def jobs(request):
    """TODO: create jobs view to list are current jobs, polish are urls so it can be more human readable,
    I'm creating and using for loop to replace spaces in post name with underscores, so title will be seen
    with underscores
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


def post(request, post_url):
    """TODO: creating post so we can sort out are jobs list, update post so it will suport underscore jobs
    searching
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

def apply_to(request):
    """TODO: creating apply view so I can render are form
    return: TODO
    """
    if request.method == 'POST':
        form = Apply(request.POST, request.FILES)
        if form.is_valid():
            apply_form = form.save(commit=False)
            apply_form.save()
            messages.add_message(
                request, messages.INFO, "You have successfully applied for\
                this ongoin position. Thanks you."
            )
            return HttpResponseRedirect('/success')
    else:
        form = Apply()
    t = loader.get_template('blog/apply_to.html')
    c = RequestContext(
        request,
        {
            'form': form,
        }
    )
    return HttpResponse(t.render(c))


def success(request):
    """TODO: create success views, we will display some information for are users
    return: TODO
    """
    return render_to_response(
        'blog/success.html',
        context_instance=RequestContext(request)
    )
