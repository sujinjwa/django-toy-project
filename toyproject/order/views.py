from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .paginations import OrderPagination

# Create your views here.
class OrderListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

    def get_queryset(self):
        orders = Order.objects.all()
        return orders

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)