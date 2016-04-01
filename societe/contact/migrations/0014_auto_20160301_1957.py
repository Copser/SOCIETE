# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_contactform_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(),
        ),
    ]
