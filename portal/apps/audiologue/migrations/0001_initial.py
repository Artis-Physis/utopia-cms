# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-18 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'audiologue', verbose_name='audio')),
                ('title', models.CharField(max_length=255, verbose_name='t\xedtulo')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='slug')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='pie')),
                ('byline', models.CharField(blank=True, max_length=255, null=True, verbose_name='autor/es')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripci\xf3n')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, null=True, verbose_name='fecha de subida')),
                ('times_viewed', models.PositiveIntegerField(default=0, editable=False, verbose_name='visto')),
                ('is_public', models.BooleanField(default=True, verbose_name='p\xfablico')),
            ],
        ),
    ]
