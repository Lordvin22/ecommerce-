# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product2)
admin.site.register(PurchaseCartOK)
admin.site.register(Cart)
admin.site.register(StatusPurchase)
admin.site.register(User)