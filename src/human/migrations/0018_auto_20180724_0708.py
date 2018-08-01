# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-24 07:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human', '0017_remove_choice_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default='h', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
