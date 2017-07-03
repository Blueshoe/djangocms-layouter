# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layouter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerplugin',
            name='equal_height',
            field=models.BooleanField(verbose_name='Align Content Height', default=False, help_text='Align height of all columns in this row. Please note: This setting is not  supported by Internet Explorer 9 and below.'),
        ),
    ]
