# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsAdvertisment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('jobs_advertisment_title', models.CharField(max_length=225)),
                ('jobs_advertisment_desctiption', models.TextField()),
                ('jobs_categories', models.CharField(choices=[('1', 'Carpenter'), ('2', 'Housekepp'), ('3', 'Plumbing'), ('4', 'Electrical'), ('5', 'Construction'), ('6', 'HVAC')], max_length=1)),
                ('jobs_advertisment_created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-jobs_advertisment_created_at'],
            },
        ),
    ]
