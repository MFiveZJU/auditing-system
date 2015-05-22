# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(serialize=False, primary_key=True)),
                ('report_info', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UnverifiedBill',
            fields=[
                ('bill_id', models.IntegerField(serialize=False, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('buyer_name', models.CharField(max_length=128)),
                ('seller_name', models.CharField(max_length=128)),
                ('goods_quantity', models.IntegerField()),
                ('goods_unit_price', models.FloatField()),
                ('supposed_to_pay', models.FloatField()),
                ('actually_paid', models.FloatField()),
                ('transaction_time', models.DateTimeField()),
                ('extra_info', models.CharField(max_length=256)),
                ('bill_generated_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerifiedBill',
            fields=[
                ('bill_id', models.IntegerField(serialize=False, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('buyer_name', models.CharField(max_length=128)),
                ('seller_name', models.CharField(max_length=128)),
                ('goods_quantity', models.IntegerField()),
                ('goods_unit_price', models.FloatField()),
                ('supposed_to_pay', models.FloatField()),
                ('actually_paid', models.FloatField()),
                ('transaction_time', models.DateTimeField()),
                ('extra_info', models.CharField(max_length=256)),
                ('is_valid', models.BooleanField()),
                ('bill_generated_time', models.DateTimeField()),
                ('bill_verified_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillReport',
            fields=[
                ('bill_id', models.OneToOneField(to='bill_verification.VerifiedBill', primary_key=True, serialize=False)),
                ('report_id', models.OneToOneField(to='bill_verification.Report', primary_key=True)),
            ],
        ),
    ]
