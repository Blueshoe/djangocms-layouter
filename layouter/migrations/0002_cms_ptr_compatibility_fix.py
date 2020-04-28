# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layouter', '0001_squashed_0001_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='layouter_containerplugin', auto_created=True,
                                  primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)
        ),
    ]
