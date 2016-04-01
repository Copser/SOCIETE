# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0005_userprofile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='email',
            new_name='website',
        ),
    ]
