# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('GDG', 'Gestion Directiva'), ('SIC', 'Sistema Integrado de Calidad'), ('COM', 'Compras'), ('LOG', 'Logistica'), ('COM', 'Comercial'), ('SER', 'Servicio al Cliente'), ('APO', 'Apoyo')], max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=100)),
                ('archive', models.FileField(upload_to='docuemntos/')),
            ],
            options={
                'verbose_name_plural': 'Archivos',
                'ordering': ['nombre'],
            },
        ),
    ]
