# Generated by Django 5.0.4 on 2024-04-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='centrosBip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea', models.CharField(max_length=100)),
                ('estacion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('este', models.FloatField()),
                ('norte', models.FloatField()),
                ('longitud', models.FloatField()),
                ('latitud', models.FloatField()),
            ],
        ),
    ]
