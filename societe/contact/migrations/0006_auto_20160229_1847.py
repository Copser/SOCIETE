# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20160217_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='birthdate',
            new_name='birthday',
        ),
    ]
