# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('email', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('first_name', models.CharField(max_length=30, default=None)),
                ('last_name', models.CharField(max_length=30, default=None)),
                ('gender', models.CharField(max_length=10, default=None)),
                ('phone_number', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'MyUser',
            },
        ),
    ]
