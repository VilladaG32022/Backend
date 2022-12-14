# Generated by Django 4.1.1 on 2022-11-29 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0043_alter_inventory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('kg', 'Kilogramos'), ('gr', 'Gramos'), ('ml', 'Mililitros'), ('lt', 'Litros'), ('U', 'Unidades')], default='U', max_length=2, verbose_name='Tipo de unidad'),
        ),
    ]
