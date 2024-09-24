# Generated by Django 5.1.1 on 2024-09-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_serial_number', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('operator_airline', models.DateField()),
                ('number_of_engines', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('callsign', models.CharField(max_length=100)),
                ('founded_year', models.IntegerField()),
                ('base_airport', models.CharField(max_length=100)),
            ],
        ),
    ]
