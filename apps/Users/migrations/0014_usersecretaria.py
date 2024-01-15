# Generated by Django 5.0.1 on 2024-01-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_alter_user_numero_identidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSecretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('numero_identidad', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
    ]
