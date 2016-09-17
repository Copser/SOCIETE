# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplySuperForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('telephone', models.CharField(max_length=250, blank=True)),
                ('mobile', models.CharField(max_length=250)),
                ('birthday', models.DateField(null=True)),
                ('experience', models.TextField()),
                ('references', models.TextField()),
                ('hourly_rate', models.CharField(max_length=100)),
                ('licences', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
