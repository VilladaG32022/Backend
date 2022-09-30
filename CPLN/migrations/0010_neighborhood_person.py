# Generated by Django 4.1.1 on 2022-09-30 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0009_remove_person_neighborhood_delete_neighborhood_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(default='sin direccion', max_length=100)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('is_candidate', models.BooleanField(default=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.neighborhood')),
            ],
        ),
    ]