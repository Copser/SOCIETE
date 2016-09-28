# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superapplyform',
            name='working_hours',
            field=models.IntegerField(),
        ),
    ]
