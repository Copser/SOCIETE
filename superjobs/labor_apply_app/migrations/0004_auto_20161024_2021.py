# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor_apply_app', '0003_personalinfo_curriculum_vitae'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='hourly_wage',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
