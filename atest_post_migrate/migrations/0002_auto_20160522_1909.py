# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-05-22 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atest_post_migrate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='field',
            new_name='new_field',
        ),
    ]
