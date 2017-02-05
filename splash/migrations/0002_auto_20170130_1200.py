# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'Creation Date')),
                ('end', models.DateTimeField(verbose_name=b'Creation Date')),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipmentID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
                ('fileID', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Formulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('formulationID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='PageRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'Creation Date')),
                ('end', models.DateTimeField(verbose_name=b'Creation Date')),
                ('notebookID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scientistID', models.CharField(max_length=256)),
                ('valaEntry', models.ForeignKey(to='splash.ValaEntry')),
            ],
        ),
        migrations.RenameModel(
            old_name='ValaEntryExperimentType',
            new_name='ExperimentType',
        ),
        migrations.RenameModel(
            old_name='ValaEntryStatus',
            new_name='FileType',
        ),
        migrations.RenameModel(
            old_name='ValaEntryFileType',
            new_name='Status',
        ),
        migrations.RemoveField(
            model_name='valaentrydate',
            name='valaEntry',
        ),
        migrations.RemoveField(
            model_name='valaentryequipment',
            name='valaEntry',
        ),
        migrations.RemoveField(
            model_name='valaentryfile',
            name='fileType',
        ),
        migrations.RemoveField(
            model_name='valaentryfile',
            name='valaEntry',
        ),
        migrations.RemoveField(
            model_name='valaentryformulation',
            name='valaEntry',
        ),
        migrations.RemoveField(
            model_name='valaentrypagerange',
            name='valaEntry',
        ),
        migrations.RemoveField(
            model_name='valaentryscientist',
            name='valaEntry',
        ),
        migrations.RenameField(
            model_name='experimenttype',
            old_name='string',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='filetype',
            old_name='string',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='string',
            new_name='text',
        ),
        migrations.DeleteModel(
            name='ValaEntryDate',
        ),
        migrations.DeleteModel(
            name='ValaEntryEquipment',
        ),
        migrations.DeleteModel(
            name='ValaEntryFile',
        ),
        migrations.DeleteModel(
            name='ValaEntryFormulation',
        ),
        migrations.DeleteModel(
            name='ValaEntryPageRange',
        ),
        migrations.DeleteModel(
            name='ValaEntryScientist',
        ),
        migrations.AddField(
            model_name='file',
            name='fileType',
            field=models.ForeignKey(to='splash.FileType'),
        ),
        migrations.AddField(
            model_name='file',
            name='valaEntry',
            field=models.ForeignKey(to='splash.ValaEntry'),
        ),
    ]
