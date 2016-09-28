# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperApplyForm',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('hourly_rate', models.IntegerField()),
                ('working_hours', models.IntegerField(max_length=100)),
                ('drivers_license', models.CharField(max_length=100)),
                ('curriculum_vitae', models.FileField(upload_to='CV')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SuperExperience',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('work_experience', models.TextField()),
                ('hospitality', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SuperReference',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_phone', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='superapplyform',
            name='previous_job',
            field=models.ForeignKey(to='super_apply.SuperReference'),
        ),
        migrations.AddField(
            model_name='superapplyform',
            name='relevante_experience',
            field=models.ForeignKey(to='super_apply.SuperExperience'),
        ),
    ]
