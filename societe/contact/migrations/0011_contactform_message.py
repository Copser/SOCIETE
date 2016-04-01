# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_remove_contactform_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.CharField(blank=True, max_length=4000),
        ),
    ]
