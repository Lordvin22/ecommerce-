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
    password = models.CharField(max_length=50)
    sucess = models.BooleanField(default=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.username)


class Log(models.Model):
    id_user = models.ManyToManyField(User)
    sentence = models.CharField(max_length=100)


class Purchase(models.Model):
    id_product = models.ForeignKey(Product2, on_delete=models.CASCADE, blank=True, default=True)
    id_user = models.ManyToManyField(User)
    status = models.IntegerField(blank=True)

    def __unicode__(self):
        return '{}'.format(self.id_product)


class Cart(models.Model):
    id_purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=True, default=True)
    quantity = models.IntegerField()