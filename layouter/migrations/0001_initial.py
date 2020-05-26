# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='layouter_containerplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('container_type', models.IntegerField(default=[100], choices=[(0, 'One tile - full width'), (1, 'Two tiles - 50 | 50'), (2, 'Two tiles - 25 | 75'), (3, 'Two tiles - 75 | 25'), (4, 'Two tiles - 33 | 66'), (5, 'Two tiles - 66 | 33'), (6, 'Three tiles - 33 | 33 | 33'), (7, 'Three tiles - 25 | 25 | 50'), (8, 'Three tiles - 25 | 50 | 25'), (9, 'Three tiles - 50 | 25 | 25'), (10, 'Four tiles - 25 | 25 | 25 | 25')])),
                ('margin', models.IntegerField(default=0, help_text='How much margin is needed on the left and right side?', choices=[(0, 'No margin'), (1, b'8.33%'), (2, b'16.66%'), (3, b'25%'), (4, b'33.33%')])),
                ('css_classes', models.CharField(max_length=512, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
