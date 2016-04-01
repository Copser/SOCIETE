import os
from uuid import uuid4

from django.db import models


class ReviewCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    codename = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """doc"""
        return str(self.name)

    class Meta:
        verbose_name_plural = "Review categories"


class ReviewBase(models.Model):
    """doc"""
    def directory_path(instance, filename):
        """doc"""
        return '{0}/{1}{2}'.format(
            'reviews',
            uuid4(),
            os.path.splitext(filename)[1])

    photo = models.ImageField(
        upload_to=directory_path, blank=False)
    url = models.URLField("Link", blank=True, null=True)
    name = models.CharField(max_length=100, blank=False)

    message = models.TextField(max_length=255, blank=False)
    category = models.ForeignKey(ReviewCategory)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """doc"""
        return "Review #{0} - {1}".format(self.id, str(self.name.capitalize()))

    class Meta:
        abstract = True


class OnMapReview(ReviewBase):
    position_x = models.PositiveSmallIntegerField(default=0)
    position_y = models.PositiveSmallIntegerField(default=0)


class OnMapReviewLayout(models.Model):
    reviews = models.ManyToManyField(OnMapReview)
    category = models.ForeignKey(ReviewCategory)

    def __str__(self):
        """doc"""
        return "Layout #{0} - {1}".format(self.id, str(self.category).capitalize())
