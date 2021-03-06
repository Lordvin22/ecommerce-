from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from products.viewsets import *


urlpatterns = [
    url(r'^v1/productlist', Product2ViewSets, name='product_set'),
    url(r'^v1/products/$', ProductList.as_view(), name='product_list'),
    url(r'^v1/add_products/$', CreateProduct.as_view(), name='product_add'),
    url(r'^v1/get_productid/(?P<id>.+)', GetProductId.as_view(), name='get_productid'),
    url(r'^v1/get_productdetail/(?P<pk>[0-9]+)/$', ProductoDetalle.as_view()),
    url(r'^v1/cart/$', createCart, name='getCart'),
    url(r'^v1/purchase1/$', PurchaseCartCreate, name='get_purchase'),

    url(r'^v1/purchaselist/$', PurchaseCartList.as_view(), name='get_purchaselist'),
    #url(r'^v1/products/(?P<pk>.+)/get_purchasedetail/(?P<pk1>[0-9]+)/$', PurchaseCart.as_view()),
    url(r'^v1/get_productname/(?P<name>.+)/$', GetProductName.as_view(),name='get_productname'),
    url(r'^v3/user/$', UserCreate.as_view(), name='user_create'),
    url(r'^v3/usertype/$', UserType.as_view(), name='user_list'),
    url(r'^v1/products/(?P<pk>.+)/cart/', CartCreate.as_view(), name='get_cart'),

    url(r'^v3/userjavi/', Javi.as_view(), name='user_create'),
    url(r'^v3/getuser/', GetUser.as_view(), name='user_create'),
    url(r'^v3/getuserproducts/$', getPurchaseCartHistory, name='getPurchaseHistory'),
    url(r'^v3/getcart/$', computeTicketValue, name='getCart'),
    url(r'^v3/buyproduct/$', BuyProduct, name='buyproduct'),
    url(r'^v3/getCartlist/$', GetCart.as_view(), name='buyproduct'),

]








