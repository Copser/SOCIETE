# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=225)),
                ('mobile', models.CharField(max_length=225)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('previous_company_name', models.CharField(max_length=225)),
                ('previous_company_email', models.CharField(max_length=225)),
                ('previous_job_title', models.CharField(max_length=225)),
                ('jobs_experience', models.TextField()),
                ('hospitality_relations_experience', models.TextField()),
                ('working_hours', models.CharField(max_length=225)),
                ('choose_desired_working_hours_wage', models.DecimalField(max_digits=2, decimal_places=0)),
                ('type_of_driver_licences', models.CharField(max_length=1, choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'), ('5', 'E'), ('6', 'M')])),
                ('applicants_cv', models.FileField(upload_to='CV/')),
                ('applicants_timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('applicants_timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('categories', models.CharField(default=1, max_length=1, choices=[(1, 'Carpenter'), (2, 'Housekeep'), (3, 'Plumbing'), (4, 'Electrical'), (5, 'Construction'), (6, 'HVAC')])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('tag', models.CharField(max_length=20, blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
