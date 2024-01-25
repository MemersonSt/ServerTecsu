# Generated by Django 5.0.1 on 2024-01-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0015_delete_usersecretaria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudents',
            options={'verbose_name': 'ESTUDIANTE', 'verbose_name_plural': 'ESTUDIANTES'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'REPRESENTANTE', 'verbose_name_plural': 'REPRESENTANTES'},
        ),
        migrations.AddField(
            model_name='estudents',
            name='uid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='estudents',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
