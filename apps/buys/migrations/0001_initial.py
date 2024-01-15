# Generated by Django 5.0.1 on 2024-01-12 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id_shopping', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('code_students', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Shopping',
                'verbose_name_plural': 'Shoppings',
            },
        ),
        migrations.CreateModel(
            name='ShoppingDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_product', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('id_shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buys.shopping')),
            ],
            options={
                'verbose_name': 'Shopping Detail',
                'verbose_name_plural': 'Shopping Details',
            },
        ),
    ]