# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-12 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0002_auto_20180712_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, default='1999-08-28', null=True, verbose_name='birth date'),
        ),
        migrations.AlterModelTable(
            name='person',
            table='people',
        ),
    ]
