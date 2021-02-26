# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-26 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_auto_20160107_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='users',
        ),
        migrations.RemoveField(
            model_name='partneraddress',
            name='country',
        ),
        migrations.RemoveField(
            model_name='partneraddress',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='stockalert',
            name='stockrecord',
        ),
        migrations.AlterUniqueTogether(
            name='stockrecord',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='stockrecord',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='stockrecord',
            name='product',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.DeleteModel(
            name='PartnerAddress',
        ),
        migrations.DeleteModel(
            name='StockAlert',
        ),
        migrations.DeleteModel(
            name='StockRecord',
        ),
    ]
