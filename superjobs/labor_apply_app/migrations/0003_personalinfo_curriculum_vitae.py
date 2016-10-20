# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labor_apply_app', '0002_auto_20161018_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='curriculum_vitae',
            field=models.FileField(default=datetime.datetime(2016, 10, 19, 18, 10, 34, 266100, tzinfo=utc), upload_to='cv/'),
            preserve_default=False,
        ),
    ]
