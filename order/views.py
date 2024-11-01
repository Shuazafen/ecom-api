from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class Order(APIView):
    def get(request, format=None):
        obj = Order.objects.all()
        serializers = OrderSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK) 