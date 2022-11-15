# Generated by Django 4.1.1 on 2022-11-10 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0037_alter_familyvolunteer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventario', 'verbose_name_plural': 'Inventarios'},
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='id_family',
        ),
        migrations.AddField(
            model_name='familyvolunteer',
            name='id_inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CPLN.inventory', verbose_name='Inventario'),
        ),
    ]
