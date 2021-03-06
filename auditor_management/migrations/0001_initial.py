# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditor',
            fields=[
                ('auditor_id', models.IntegerField(serialize=False, primary_key=True, auto_created=True)),
                ('auditor_email', models.CharField(max_length=32)),
                ('auditor_name', models.CharField(max_length=32)),
                ('auditor_password', models.CharField(max_length=16)),
                ('auditor_phone', models.IntegerField()),
                ('auditor_info', models.CharField(blank=True, max_length=256)),
                ('email_confirmed', models.BooleanField()),
                ('administrator_confirmed', models.BooleanField()),
            ],
        ),
    ]
