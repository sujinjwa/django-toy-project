from rest_framework import status # 상태 코드 반환하기 위한 프레임워크
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Order

# Create your views here.
class OrderListView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()

        return render(request, 'order_list.html', {'orders': orders})