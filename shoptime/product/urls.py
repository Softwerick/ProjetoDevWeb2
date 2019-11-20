from django.conf.urls import url
 
from .views import ProductList, ProductDestroy, ProductCreate, ProductUpdate, ProductGet, ProviderList
 
urlpatterns = [
   url(r'product/$', ProductList.as_view()),
   url(r'product/add/$', ProductCreate.as_view()),
   url(r'product/(?P<pk>\d+)/$', ProductDestroy.as_view()),
   url(r'product/edit/(?P<pk>\d+)/$', ProductUpdate.as_view()),
   url(r'product/get/(?P<pk>\d+)/$', ProductGet.as_view()),
   url(r'provider/$', ProviderList.as_view())
]
