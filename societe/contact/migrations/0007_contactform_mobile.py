# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20160229_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='mobile',
            field=models.CharField(max_length=32, default=2),
            preserve_default=False,
        ),
    ]
