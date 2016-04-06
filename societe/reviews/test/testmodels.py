from django.test import TestCase
from django.core.urlresolvers import reverse
from reviews.models import ReviewCategory


# Models test
class ReviewCategoryTest(TestCase):

    """Docstring for ReviewCategoryTest. Bulding TestCase after coverage societe application """
    def create_reviewcategory(self, name='tester', codename='intern'):
        """TODO: to be defined1. """
        return ReviewCategory.objects.create(name=name, codename=codename)

    def test_reviewcategory_creation(self):
        """TODO: Docstring for test_reviewcategory_creation.
        testing to see will name and codename be created
        :returns: TODO

        """
        w = self.create_reviewcategory()
        self.assertTrue(isinstance(w, ReviewCategory))
        self.assertEqual(w.__str__(), w.name)
