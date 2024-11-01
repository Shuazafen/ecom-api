from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import Cart, CartItem  
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import *

# Create your views here.
# class CartViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializers_class = CreateCartSerializer
#     queryset = CartItem

class CartItem(APIView):
    def get(self, request):
        obj = CartItem.objects.all()
        serializers = CartItemSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializers = CreateCartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        product = self.get_by_id(pk)
        serializers = CreateCartSerializer(product, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)