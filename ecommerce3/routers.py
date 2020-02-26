from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from products.viewsets import Product2ViewSets\
    ,ProductList, GetProductId, GetProductName,PurchaseCreate,PurchaseList, \
    UserCreate, ProductoDetalle, PurchaseDetail


urlpatterns = [
    url(r'^v1/product_set', Product2ViewSets, name='product_set'),
    url(r'^v1/products/$', ProductList.as_view(), name='product_list'),
    url(r'^v1/get_productid/(?P<id>.+)', GetProductId.as_view(), name='get_productid'),
    url(r'^v1/get_productdetail/(?P<pk>[0-9]+)/$', ProductoDetalle.as_view()),
    url(r'^v1/products/(?P<pk>.+)/purchase/', PurchaseCreate.as_view(), name='get_purchase'),
    url(r'^v1/purchaselist/$', PurchaseList.as_view(), name='get_purchaselist'),
    url(r'^v1/get_purchasedetail/(?P<pk>[0-9]+)/$', PurchaseDetail.as_view()),
    url(r'^v1/get_productname/(?P<name>.+)/$', GetProductName.as_view(),name='get_productname'),
    url(r'^v3/user/$', UserCreate.as_view(), name='user_list'),

]








