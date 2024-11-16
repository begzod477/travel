# Generated by Django 5.1.1 on 2024-11-16 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Sayohat',
                'verbose_name_plural': 'Sayohatlar',
            },
        ),
        migrations.CreateModel(
            name='TravelCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.travel')),
            ],
            options={
                'verbose_name': 'Sayohat mashinasi',
                'verbose_name_plural': 'Sayohat mashinalari',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='TravelHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotel_stars', models.IntegerField()),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.travel')),
            ],
            options={
                'verbose_name': 'Mehmonxona',
                'verbose_name_plural': 'Mehmonxonalar',
                'ordering': ['price'],
            },
        ),
    ]