from rest_framework import serializers
from orderapi.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['user_id', 'address_id', 'total_amount', 'created_at', 'updated_at']
