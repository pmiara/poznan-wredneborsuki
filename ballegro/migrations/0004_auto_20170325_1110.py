# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballegro', '0003_clothes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
    ]