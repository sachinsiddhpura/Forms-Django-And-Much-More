# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-24 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0021_choice_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='users',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]