# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor_apply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaborExperience',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('relevante_experience', models.TextField()),
                ('hospitality', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LaborReference',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_phone', models.CharField(max_length=100)),
                ('previous_job_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='laborinfo',
            name='previouse_relevant_working_references',
        ),
        migrations.RemoveField(
            model_name='laborinfo',
            name='relevante_hospitality_experience',
        ),
        migrations.RemoveField(
            model_name='laborinfo',
            name='relevante_previouse_working_experience',
        ),
        migrations.AddField(
            model_name='laborreference',
            name='labor_info',
            field=models.ForeignKey(blank=True, to='labor_apply.LaborInfo'),
        ),
        migrations.AddField(
            model_name='laborexperience',
            name='labor_info',
            field=models.ForeignKey(blank=True, to='labor_apply.LaborInfo'),
        ),
    ]
