# Generated by Django 5.0.1 on 2024-01-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_sale_client_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]