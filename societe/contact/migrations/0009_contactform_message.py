# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20160229_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]
