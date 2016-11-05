# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsApplyTo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('choose_desired_working_hours_wage', models.DecimalField(decimal_places=0, max_digits=2)),
                ('type_of_driver_licences', models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'), ('5', 'E'), ('6', 'M')], max_length=1)),
                ('applicants_cv', models.FileField(upload_to='CV/')),
                ('applicants_timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('applicants_timestamp',),
            },
        ),
    ]
