# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-15 21:51
from __future__ import unicode_literals

import django.core.validators
import oscar.models.fields.autoslugfield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20180124_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationeventtype',
            name='code',
            field=oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, help_text='Code used for looking up this event programmatically', max_length=128, populate_from='name', separator='_', unique=True, validators=[django.core.validators.RegexValidator(message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.", regex='^[a-zA-Z_][0-9a-zA-Z_]*$')], verbose_name='Code'),
        ),
    ]
