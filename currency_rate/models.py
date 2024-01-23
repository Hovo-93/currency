from django.db import models


# Create your models here.

class Currency(models.Model):
    currency_name = models.CharField(max_length=25)
    usd_to_rub_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
