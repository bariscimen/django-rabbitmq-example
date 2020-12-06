from worker.models import Invoice

from celery import shared_task


@shared_task(name='create_invoice_for_order', serializer='json')
def create_invoice_for_order(order_id, total_cost):
    Invoice.objects.create(
        order_id=order_id,
        total_amount=total_cost,
        total_taxes=total_cost * 0.18
    )
