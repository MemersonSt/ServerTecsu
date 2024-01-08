# Generated by Django 5.0.1 on 2024-01-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_identidad', models.CharField(max_length=20)),
                ('code_student', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
