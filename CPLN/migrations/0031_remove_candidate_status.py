# Generated by Django 4.1.1 on 2022-10-19 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0030_alter_candidate_telephone_alter_volunteer_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='status',
        ),
    ]