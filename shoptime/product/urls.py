from django.conf.urls import url
 
from .views import ProductList, ProductDestroy, ProductCreate
 
urlpatterns = [
   url(r'product/$', ProductList.as_view()),
   url(r'product/add/$', ProductCreate.as_view()),
   url(r'product/(?P<pk>\d+)/$', ProductDestroy.as_view()),
]
