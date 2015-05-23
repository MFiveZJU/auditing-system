from django.db import models

# Create your models here.

class UnverifiedBill(models.Model):
    # meta-options
    db_table = 'UnverifiedBill'
    # column
    bill_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    buyer_name = models.CharField(max_length=32)
    seller_name = models.CharField(max_length=32)
    goods_quantity = models.IntegerField()
    goods_unit_price = models.FloatField()
    supposed_to_pay = models.FloatField()
    actually_paid = models.FloatField()
    transaction_time = models.DateTimeField()
    extra_info = models.CharField(max_length=256)
    # timestamp, might be used for statistics
    bill_generated_time = models.DateTimeField(auto_now_add=True)


class VerifiedBill(models.Model):
    # meta-options
    db_table = 'VerifiedBill'
    # column
    bill_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    buyer_name = models.CharField(max_length=32)
    seller_name = models.CharField(max_length=32)
    goods_quantity = models.IntegerField()
    goods_unit_price = models.FloatField()
    supposed_to_pay = models.FloatField()
    actually_paid = models.FloatField()
    transaction_time = models.DateTimeField()
    extra_info = models.CharField(max_length=256)
    is_valid = models.BooleanField()
    # timestamp, might be used for statistics
    bill_generated_time = models.DateTimeField()
    bill_verified_time = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    # meta-options
    db_table = 'Report'
    # column
    report_id = models.IntegerField(primary_key=True)
    report_info = models.CharField(max_length=256)


class BillReport(models.Model):
    # meta-options
    db_table = 'BillReport'
    # column
    bill_id = models.OneToOneField(VerifiedBill)
    report_id = models.OneToOneField(Report)
    # bill_id = models.OneToOneField(VerifiedBill, related_name='report_id')
    # report_id = models.OneToOneField(Report, related_name='bill_id')
