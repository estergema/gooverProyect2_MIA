# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gooverWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='rol_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='rol_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='conductor_id',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='conductor_id',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='marca_id',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='modelo_id',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='MarcaVehiculo',
        ),
        migrations.DeleteModel(
            name='ModeloVehiculo',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
