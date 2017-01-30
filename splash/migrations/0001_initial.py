# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValaEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hypothesis', models.CharField(max_length=1024)),
                ('creationDate', models.DateTimeField(verbose_name=b'Creation Date')),
                ('projectID', models.CharField(max_length=16)),
                ('reviewer', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'Creation Date')),
                ('end', models.DateTimeField(verbose_name=b'Creation Date')),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryEquipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipmentID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryExperimentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField()),
                ('string', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
                ('fileID', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryFileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField()),
                ('string', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryFormulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('formulationID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryPageRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'Creation Date')),
                ('end', models.DateTimeField(verbose_name=b'Creation Date')),
                ('notebookID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryScientist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scientistID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ValaEntryStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField()),
                ('string', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='valaentryfile',
            name='fileType',
            field=models.ForeignKey(to='splash.ValaEntryFileType'),
        ),
        migrations.AddField(
            model_name='valaentryfile',
            name='valaEntry',
            field=models.ForeignKey(to='splash.ValaEntry'),
        ),
        migrations.AddField(
            model_name='valaentry',
            name='experimentType',
            field=models.ForeignKey(to='splash.ValaEntryExperimentType'),
        ),
        migrations.AddField(
            model_name='valaentry',
            name='status',
            field=models.ForeignKey(to='splash.ValaEntryStatus'),
        ),
    ]
