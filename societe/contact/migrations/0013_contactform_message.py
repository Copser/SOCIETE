# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_remove_contactform_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]
