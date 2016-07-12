# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20160710_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=225, default=datetime.datetime(2016, 7, 12, 17, 51, 16, 437319, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
