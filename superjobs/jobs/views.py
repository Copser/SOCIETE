from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import get_object_or_404

from .models import Job, ApplyToJob

# Create your views here.
def jobs(request):
    """TODO: representing are jobs
    return: TODO
    """
    latest_jobs = Job.objects.all().order_by('-job_created_at')
    t = loader.get_template('job/jobs.html')
    context_dict = {'latest_jobs': latest_jobs, }
    for job in latest_jobs:
        job.url = job.job_title.replace(' ', '_')
    c = Context(context_dict)
    return HttpResponse(t.render(c))
