from rest_framework import serializers
from worker.models import Invoice


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['order_id', 'user_id', 'total_amount', 'total_taxes', 'created_at', 'updated_at']
