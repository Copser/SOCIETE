# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentFee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('stripe_id', models.CharField(max_length=40, blank=True)),
                ('user_rec', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'fee',
            },
        ),
    ]
