# Generated by Django 4.1.1 on 2022-11-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0035_alter_volunteer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('kg', 'Kilogramos'), ('gr', 'Gramos'), ('mm', 'Mililitros'), ('lt', 'Litros'), ('u', 'Unidades')], default='u', max_length=2, verbose_name='Tipo de unidad'),
        ),
    ]
