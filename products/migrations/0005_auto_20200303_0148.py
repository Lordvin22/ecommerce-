# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-03 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200303_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.StatusPurchase'),
        ),
    ]