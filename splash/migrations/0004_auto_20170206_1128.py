# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0003_auto_20170206_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filetype',
            options={'verbose_name_plural': 'FileTypes'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='valaentry',
            options={'verbose_name_plural': 'ValaEntries'},
        ),
    ]
