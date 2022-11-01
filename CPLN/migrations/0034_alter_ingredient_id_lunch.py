# Generated by Django 4.1.1 on 2022-10-27 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0033_candidate_status_delete_volunteer_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='id_lunch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='CPLN.lunch', verbose_name='Almuerzo'),
        ),
    ]