# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_userinformation_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='other_names',
            new_name='last_name',
        ),
    ]
