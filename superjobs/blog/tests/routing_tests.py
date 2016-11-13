from django.test import TestCase
from django.core.urlresolvers import resolve
from blog.views import jobs


class JobsPageTest(TestCase):
    """TODO: testing blog/ routing, we want to see if are pages are
    wired correctly
    return: TODO
    """
    def test_jobs_resolvers_to_jobs_view(self):
        """TODO: should return jobs page
        return: TODO
        """
        jobs_page = resolve('/blog/jobs/')
        self.assertEqueal(jobs_page.func, jobs)

    def test_prover_status_code(self):
        """TODO: return status code
        return: TODO
        """
        jobs = self.client.get('/blog/jobs/')
        self.assertEqueals(jobs.status_code, 200)
