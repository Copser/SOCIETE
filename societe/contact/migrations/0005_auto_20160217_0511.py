# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20160217_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contactform',
            name='last_name',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]
