# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_paymentuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentUser',
            new_name='User',
        ),
    ]
