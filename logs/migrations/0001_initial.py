# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_id', models.IntegerField(default=0)),
                ('log_open', models.BooleanField(default=False)),
                ('log_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
