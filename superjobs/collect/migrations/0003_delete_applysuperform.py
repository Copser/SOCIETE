# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_remove_applysuperform_birthday'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApplySuperForm',
        ),
    ]
