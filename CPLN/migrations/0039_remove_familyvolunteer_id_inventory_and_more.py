# Generated by Django 4.1.1 on 2022-11-10 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0038_alter_inventory_options_remove_inventory_id_family_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyvolunteer',
            name='id_inventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='id_family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CPLN.family', verbose_name='Familia'),
        ),
    ]
