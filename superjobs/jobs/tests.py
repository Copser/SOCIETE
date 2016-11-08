from django.test import TestCase
from jobs.models import Job

# Create your tests here.
class JobTests(TestCase):
    """TODO: writing small db unittests for Job model
    return: TODO
    """
    def test_str(self):
        jobs_title = Job(
            job_title="Title for a Job"
        )
        self.assertEquals(
            str(jobs_title), 'Title for a Job'
        )
