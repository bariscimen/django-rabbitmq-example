from rest_framework import viewsets

from orderapi.models import Order
from orderapi.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
