# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InitialCharacteristicModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=225, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=225, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=225, verbose_name='Email')),
                ('birthday', models.DateField(verbose_name='Birthday', null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('move_in_date', models.DateField(verbose_name='Move in date', null=True)),
                ('move_out_date', models.DateField(verbose_name='Move out date', null=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'InitialCharacteristicModels',
                'verbose_name': 'InitialCharacteristicModel',
                'ordering': ('-timestamp',),
            },
        ),
    ]
