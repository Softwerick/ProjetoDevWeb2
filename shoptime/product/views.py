from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
 
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
