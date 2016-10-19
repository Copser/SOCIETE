# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('previous_company_name', models.CharField(max_length=255)),
                ('previous_company_email', models.CharField(max_length=255)),
                ('previous_company_phone', models.CharField(max_length=255)),
                ('previous_job_title', models.CharField(max_length=255)),
                ('relevante_experience', models.TextField()),
                ('hospitality_experience', models.TextField()),
                ('future_working_hourse', models.CharField(max_length=225)),
                ('hourly_rate', models.DecimalField(max_digits=2, decimal_places=2)),
                ('driver_license', models.CharField(choices=[('A', 'B'), ('C', 'D'), ('E', 'None')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
