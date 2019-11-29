from django.db import transaction
from rest_framework import serializers
from .models import Product, Provider, ProductProvider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'weight', 'price', 'stock', 'providers')

    @transaction.atomic
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        if "providers" in self.initial_data:
            providers = self.initial_data.get("providers")
            for provider in providers:
                provider_instance = Provider.objects.get(pk=provider)
                ProductProvider(product=product, provider=provider_instance).save()
            product.save()
            return product

    @transaction.atomic
    def update(self, instance, validated_data):
        providers = self.initial_data.get("providers")
        instance.providers.clear()
        for provider in providers:
                provider_instance = Provider.objects.get(pk=provider)
                ProductProvider(product=instance, provider=provider_instance).save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



