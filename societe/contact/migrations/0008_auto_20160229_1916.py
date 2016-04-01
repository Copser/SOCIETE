# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_contactform_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='mobile',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
