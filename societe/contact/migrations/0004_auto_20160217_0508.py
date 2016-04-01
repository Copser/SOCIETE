# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contactform_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='topic',
        ),
    ]
