# Generated by Django 4.1.1 on 2022-09-29 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPLN', '0006_remove_saucequantity_sandwich_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='lunchroom',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='lunch',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='product',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='warehouse',
        ),
        migrations.RemoveField(
            model_name='lunchroom',
            name='address',
        ),
        migrations.RemoveField(
            model_name='lunchroom',
            name='warehouse',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='donation',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='iproduct',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='lunchroom',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='person',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='role',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='address',
        ),
        migrations.RemoveField(
            model_name='weeklymenu',
            name='lunch',
        ),
        migrations.RemoveField(
            model_name='weeklymenu',
            name='lunchroom',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='volunteer',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.DeleteModel(
            name='Lunch',
        ),
        migrations.DeleteModel(
            name='Lunchroom',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.DeleteModel(
            name='WeeklyMenu',
        ),
        migrations.DeleteModel(
            name='Withdrawal',
        ),
    ]
