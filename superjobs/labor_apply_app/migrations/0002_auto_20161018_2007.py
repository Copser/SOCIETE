# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor_apply_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='future_working_hourse',
            new_name='future_working_hours',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='hourly_rate',
            new_name='hourly_wage',
        ),
    ]
