# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0006_auto_20170212_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valaentry',
            name='experimentType',
            field=models.ForeignKey(to='splash.ExperimentType', null=True),
        ),
        migrations.AlterField(
            model_name='valaentry',
            name='hypothesis',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='valaentry',
            name='projectID',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='valaentry',
            name='reviewer',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
