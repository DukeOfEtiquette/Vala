# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0007_auto_20170305_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valaentry',
            name='projectID',
            field=models.CharField(max_length=16),
        ),
    ]
