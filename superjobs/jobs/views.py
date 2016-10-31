from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

from .models import CarpenterAd

# Create your views here.
def carpenterjobs(request):
    """TODO: define and render CarpenterAd job
    return: TODO
    """
    latest_jobs = CarpenterAd.objects.all().order_by('-created_at')
    t = loader.get_template('jobs/carpenter_apply_now.html')
    c = Context({'latest_jobs': latest_jobs, })
    return HttpResponse(t.render(c))
