# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labor_apply_app', '0004_auto_20161024_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='owner',
            field=models.ForeignKey(related_name='info', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
