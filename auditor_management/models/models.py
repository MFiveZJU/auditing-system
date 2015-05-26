from django.db import models

class Auditor(models.Model):
    # meta-options
    db_table = 'Auditor'

    auditor_id = models.IntegerField(primary_key=True, auto_created=True)
    auditor_email = models.CharField(max_length=32)
    auditor_name = models.CharField(max_length=32)
    auditor_password = models.CharField(max_length=16)
    auditor_phone = models.IntegerField()
    auditor_info = models.CharField(max_length=256)
    email_confirmed = models.BooleanField()
    administrator_confirmed = models.BooleanField()

