from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Product, Provider
from .serializers import ProductSerializer, ProviderSerializer
 
class ProductList(generics.ListAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   permission_classes = ()
 
class ProductDestroy(generics.DestroyAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   permission_classes = (
       permissions.IsAuthenticated,
   )

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()

class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ProductGet(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   permission_classes = ()


class ProviderList(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = ()

