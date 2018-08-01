# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-12 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=100, verbose_name='middle name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='last name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('website', models.URLField(blank=True, verbose_name='website')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.AlterField(
            model_name='persontype',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='person_types',
            field=models.ManyToManyField(blank=True, to='human.PersonType'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(blank=True, help_text='If the person is an existing user of your site.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
