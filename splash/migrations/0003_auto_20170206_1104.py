# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0002_auto_20170130_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='loc',
            field=models.CharField(default=b'here', max_length=256),
        ),
        migrations.AddField(
            model_name='equipment',
            name='name',
            field=models.CharField(default=b'goggles', max_length=256),
        ),
        migrations.AlterField(
            model_name='valaentry',
            name='status',
            field=models.ForeignKey(to='splash.Status'),
        ),
    ]
