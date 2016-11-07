from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from .models import JobsAdvertisment, JobsApplyTo

# Create your views here.
def jobs_guide(request):
    """TODO: define jobs views which need to represent are jobs, you will be able to
    browse which job you want to apply, using function based views
    return:TODO
    """
    latest_jobs = JobsAdvertisment.objects.all().order_by('-jobs_advertisment_created_at')
    t = loader.get_template('jobs_guide.html')
    c = Context({'latest_jobs': latest_jobs, })
    return HttpResponse(t.render(c))
