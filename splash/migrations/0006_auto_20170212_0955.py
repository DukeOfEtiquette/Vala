# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AlterField(
            model_name='valaentry',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
