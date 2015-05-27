from django.db import models


# Create your models here.
class Auditor(models.Model):
    # meta-options
    db_table = 'Auditor'

    auditor_id = models.IntegerField(primary_key=True, auto_created=True)
    auditor_email = models.CharField(max_length=32)
    auditor_name = models.CharField(max_length=32)
    auditor_password = models.CharField(max_length=16)
    auditor_phone = models.IntegerField()
    auditor_info = models.CharField(max_length=256, blank=True)
    email_confirmed = models.BooleanField()
    administrator_confirmed = models.BooleanField()

    # Auditor(auditor_email='wqstu1@163.com', auditor_name='StephenW', auditor_password='123456', auditor_phone='15267019518')