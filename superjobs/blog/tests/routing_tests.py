from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response
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
        jobs_page = resolve('/blog/jobs')
        self.assertEqueal(jobs_page.func, jobs)

    def test_valid_status_code(self):
        """TODO: return status code, and verify jobs html page
        return: TODO
        """
        jobs = self.client.get('/blog/jobs')
        self.assertEqueals(jobs.status_code, 200)
        self.asertTemplateUser(jobs, "jobs.html")

    def test_returns_exact_html(self):
        """TODO: expend templates test so it can confirme are we
        using proper template
        return: TODO
        """
        jobs = self.client.get('/blog/jobs')
        self.assertEqueal(
            jobs.content,
            render_to_response("jobs.html").content
        )
