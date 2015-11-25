# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dist_id', models.IntegerField(default=0)),
                ('dist_distance', models.IntegerField(default=0)),
                ('dist_date', models.DateTimeField(verbose_name=b'date published', blank=True)),
            ],
        ),
    ]
