# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-24 06:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0014_auto_20180724_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]