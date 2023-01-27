from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Order, Comment
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
from .paginations import OrderPagination

# Create your views here.
class OrderListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

    def get_queryset(self):
        orders = Order.objects.all().order_by('-id')
        return orders

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, pk, *args, **kwargs):
        # print(pk) # 1
        return self.retrieve(request, args, kwargs) 
    
class CommentListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class CommentDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('-id')

    def delete(self, request, pk, *args, **kwargs):
        print(pk)
        return self.destroy(request, args, kwargs)