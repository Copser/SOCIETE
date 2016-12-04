import pytest

from blog.models import Post, Apply


pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestCaseModel():
    """TODO: Testing are model database, I will use pytest.marks
    because I need to access my database, @pytest.mark.django_db
    return: TODO
    """
    pytestmark = pytest.mark.django_db
    def test_jobs_post_field_create(self):
        """TODO: testing post field, will be create correctly
        return: TODO
        """
        post_jobs = Post(title="TestJob",
                         description="We need you!",
                         tag="plumbing, housekeep",
                        slug="test-job")
        post_jobs.save()
        assert post_jobs.title == "TestJob"
        assert post_jobs.description == "We need you!"
        assert post_jobs.tag == "plumbing, housekeep"
        assert post_jobs.slug == "testjob"

    def test_str_method_return_self_title(self):
        """TODO: testing will __str__ method return title
        return: TODO
        """
        post_method = Post(title="My Job Title")
        assert str(post_method) == post_method.title

