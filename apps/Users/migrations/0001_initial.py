# Generated by Django 5.0.1 on 2024-01-26 20:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_representante', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cedula')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'REPRESENTANTE',
                'verbose_name_plural': 'REPRESENTANTES',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_estudiante', models.CharField(max_length=255)),
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('balance', models.FloatField(default=0)),
                ('state', models.BooleanField(default=True)),
                ('Representative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.representative')),
                ('ggroups', models.ManyToManyField(related_name='student_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='student_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'ESTUDIANTE',
                'verbose_name_plural': 'ESTUDIANTES',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen de perfil')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contraseña')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_representative', models.BooleanField(default=False)),
                ('is_secretary', models.BooleanField(default=False)),
                ('is_userstore', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'REPRESENTANTE',
                'verbose_name_plural': 'REPRESENTANTES',
            },
        ),
        migrations.CreateModel(
            name='StoreUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'USUARIO DE TIENDA',
                'verbose_name_plural': 'USUARIOS DE TIENDA',
            },
        ),
        migrations.AddField(
            model_name='representative',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ADMINISTRADOR',
                'verbose_name_plural': 'ADMINISTRADORES',
            },
        ),
    ]
