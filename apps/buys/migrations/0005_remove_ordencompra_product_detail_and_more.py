# Generated by Django 5.0.1 on 2024-01-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buys', '0004_remove_itemordencompra_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordencompra',
            name='product_detail',
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='product_detail',
            field=models.ManyToManyField(blank=True, to='buys.itemordencompra'),
        ),
    ]