from celery import shared_task


@shared_task(name='create_invoice_for_order', serializer='json')
def create_invoice_for_order(order_id, total_cost):
    pass
