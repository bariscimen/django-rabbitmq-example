from django.db import models

class Invoice(models.Model):
    order_id = models.IntegerField()
    total_amount = models.FloatField()
    total_taxes = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)