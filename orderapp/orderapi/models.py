from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from orderapp.celery import app as celery_app
from .tasks import create_invoice_for_order


class Order(models.Model):
    user_id = models.IntegerField()
    address_id = models.IntegerField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Order)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        create_invoice_for_order.delay(instance.id, instance.total_amount)
