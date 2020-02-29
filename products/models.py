# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.



class Product2(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=100,blank=True)
    stock = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    sold = models.BooleanField(default=False)

    def __unicode__(self):
        return '{}'.format(self.name)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, blank=False)
    type = models.BooleanField(default=True, blank=True)


    def __unicode__(self):
        return '{}'.format(self.username)


class Log(models.Model):
    id_user = models.ManyToManyField(User)
    sentence = models.CharField(max_length=100)

class StatusPurchase(models.Model):
    description = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description



"""
CartPurchase:
    - price, product, cart, quantity 
"""


class Cart(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.user)



    """
    user_id
    price 
    
    """


class PurchaseCartOK(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product2)
    price = models.FloatField()
    quantity = models.IntegerField()