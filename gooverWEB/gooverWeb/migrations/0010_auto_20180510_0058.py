# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gooverWeb', '0009_auto_20180510_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'EFECTIVO'), ('CARD', 'TARJETA_CREDITO'), ('VIRTUAL', 'MONEDA_VIRTUAL')], default='CASH', max_length=10),
        ),
    ]
