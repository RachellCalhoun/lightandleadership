# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-29 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0050_auto_20190425_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eduprogram',
            name='video',
        ),
        migrations.AddField(
            model_name='eduprogram',
            name='row_style',
            field=models.CharField(choices=[('full', 'Full Row'), ('highlight', 'Highlight'), ('long_short', 'Long Short'), ('short_long', 'Short Long')], default='full', max_length=15),
        ),
    ]