# Generated by Django 5.0.1 on 2024-02-05 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_students_cedula_estudiante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='numero_identidad'),
        ),
        migrations.AlterField(
            model_name='students',
            name='uid',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]