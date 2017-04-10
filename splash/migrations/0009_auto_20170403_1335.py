# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0008_auto_20170305_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hypothesis', models.CharField(max_length=1024, null=True)),
                ('experimentType', models.ForeignKey(to='splash.ExperimentType', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='valaentry',
            name='experimentType',
        ),
        migrations.RemoveField(
            model_name='valaentry',
            name='hypothesis',
        ),
        migrations.AddField(
            model_name='experimentdetails',
            name='valaEntry',
            field=models.ForeignKey(to='splash.ValaEntry'),
        ),
    ]
