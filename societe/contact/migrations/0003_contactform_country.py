# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20160216_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='country',
            field=django_countries.fields.CountryField(default=2, max_length=2),
            preserve_default=False,
        ),
    ]
