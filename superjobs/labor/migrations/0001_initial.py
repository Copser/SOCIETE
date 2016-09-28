# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('hourly_rate', models.IntegerField()),
                ('working_hours', models.IntegerField()),
                ('drivers_license', models.CharField(max_length=100)),
                ('curriculum_vitae', models.FileField(upload_to='CV')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('work_experience', models.TextField()),
                ('hospitality', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_phone', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='applyform',
            name='previous_job',
            field=models.ForeignKey(to='labor.Reference'),
        ),
        migrations.AddField(
            model_name='applyform',
            name='relevante_experience',
            field=models.ForeignKey(to='labor.Experience'),
        ),
    ]
