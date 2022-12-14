# Generated by Django 4.0.6 on 2022-09-07 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(blank=True, max_length=255, null=True)),
                ('street_2', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('tower', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('observations', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_donator', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, unique=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunchroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.address')),
            ],
        ),
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
                ('age', models.IntegerField()),
                ('is_candidate', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('lunchroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.lunchroom')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.person')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.role')),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freight', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.inventory')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(blank=True, max_length=50, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.lunch')),
                ('lunchroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.lunchroom')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.address')),
            ],
        ),
        migrations.CreateModel(
            name='Userpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.person')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.donation')),
                ('iproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.product')),
            ],
        ),
        migrations.AddField(
            model_name='lunchroom',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.warehouse'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.product'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.warehouse'),
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('amount_food_cooked', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.lunch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.product')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('lunchroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.lunchroom')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPLN.neighborhood'),
        ),
    ]
