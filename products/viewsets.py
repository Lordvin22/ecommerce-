from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .serializers import Product2Serializer, UserSerializer, PurchaseSerializer
from . import serializers
from .models import Product2, User, Purchase
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins



class Product2ViewSets(viewsets.ModelViewSet):
    queryset = Product2.objects.all()
    serializer_class = serializers.Product2Serializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product2.objects.all()
    serializer_class = serializers.Product2Serializer



class ProductoDetalle(APIView):

    def get(self, request, pk):
        todo = get_object_or_404(Product2, pk=pk)
        serializer = Product2Serializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product = Product2.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class GetProductId(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Product2.objects.filter(id=self.kwargs["id"])
        return queryset

    serializer_class = Product2Serializer


class GetProductName(generics.ListAPIView):
    serializer_class = Product2Serializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = Product2.objects.all()
        name = self.request.query_params.get('name', None)
        queryset = queryset.filter(name=self.kwargs["name"])
        return queryset



class PurchaseCreate(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Purchase.objects.filter(id_product_id=self.kwargs["pk"])
        return queryset

    serializer_class = PurchaseSerializer

class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer



class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


