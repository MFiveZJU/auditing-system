# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_info', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UnverifiedBill',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('buyer_name', models.CharField(max_length=32)),
                ('seller_name', models.CharField(max_length=32)),
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
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('buyer_name', models.CharField(max_length=32)),
                ('seller_name', models.CharField(max_length=32)),
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
        migrations.AddField(
            model_name='billreport',
            name='bill_id',
            field=models.OneToOneField(to='bill_verification.VerifiedBill'),
        ),
        migrations.AddField(
            model_name='billreport',
            name='report_id',
            field=models.OneToOneField(to='bill_verification.Report'),
        ),
    ]
