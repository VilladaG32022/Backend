# Generated by Django 4.1.1 on 2022-10-05 14:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0014_remove_neighborhood_last_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField(default=datetime.date.today)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('is_candidate', models.BooleanField(default=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.neighborhood')),
            ],
        ),
        migrations.RenameModel(
            old_name='DailyCard',
            new_name='News',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]