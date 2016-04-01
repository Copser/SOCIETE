# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='move_in_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='move_out_date',
            field=models.DateField(null=True),
        ),
    ]
