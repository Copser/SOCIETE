# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_contactform_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='message',
        ),
    ]
