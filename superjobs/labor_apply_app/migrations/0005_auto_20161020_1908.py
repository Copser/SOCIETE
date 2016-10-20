# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor_apply_app', '0004_auto_20161020_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='hourly_wage',
            field=models.DecimalField(max_digits=2, decimal_places=2, default='00.00'),
        ),
    ]
