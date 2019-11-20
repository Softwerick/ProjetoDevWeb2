from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=100)
   weight = models.IntegerField()
   price = models.IntegerField()
   stock = models.IntegerField()
   providers = models.ManyToManyField('Provider', related_name='products', through='ProductProvider')
 
   def __str__(self):
       return self.name

class Provider(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.name


class ProductProvider(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)

    def __str__(self):
        return str((self.product, self.provider))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductProvider'
        verbose_name_plural = 'ProductProviders'
