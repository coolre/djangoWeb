# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_auto_20170822_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificaterecod',
            name='use',
            field=models.CharField(blank=True, max_length=160, verbose_name='备注'),
        ),
    ]
