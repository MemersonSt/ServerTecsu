# Generated by Django 5.0.1 on 2024-01-15 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buys', '0002_rename_shopping_ordencompra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemordencompra',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='buys.ordencompra'),
        ),
    ]