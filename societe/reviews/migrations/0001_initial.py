# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnMapReview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('photo', models.ImageField(upload_to=reviews.models.ReviewBase.directory_path)),
                ('url', models.URLField(null=True, blank=True, verbose_name='Link')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('position_x', models.PositiveSmallIntegerField(default=0)),
                ('position_y', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OnMapReviewLayout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('codename', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Review categories',
            },
        ),
        migrations.AddField(
            model_name='onmapreviewlayout',
            name='category',
            field=models.ForeignKey(to='reviews.ReviewCategory'),
        ),
        migrations.AddField(
            model_name='onmapreviewlayout',
            name='reviews',
            field=models.ManyToManyField(to='reviews.OnMapReview'),
        ),
        migrations.AddField(
            model_name='onmapreview',
            name='category',
            field=models.ForeignKey(to='reviews.ReviewCategory'),
        ),
    ]
