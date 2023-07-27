from django.db import models


# Create your models here.

class Concession(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    amount = models.FloatField()
    equivalent_support = models.FloatField()
    budgetary_application = models.CharField(max_length=200)
    date_of_concession = models.DateTimeField("Date published")
    subsidy = models.JSONField()
    regulatory_bases_address = models.CharField(max_length=200)
    support_type = models.JSONField()
