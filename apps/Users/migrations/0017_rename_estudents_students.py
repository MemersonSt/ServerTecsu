# Generated by Django 5.0.1 on 2024-01-24 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_alter_estudents_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudents',
            new_name='Students',
        ),
    ]
