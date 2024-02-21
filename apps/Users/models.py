from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

    def create_storeuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, False, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True, )
    name = models.CharField('Nombres', max_length=50, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    number_phone = models.CharField('Número de teléfono', max_length=20, blank=True, null=True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)
    numero_identidad = models.CharField('Número de identidad', max_length=20, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

    class Meta:
        verbose_name = 'REPRESENTANTE'
        verbose_name_plural = 'REPRESENTANTES'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Students(models.Model):
    cedula_estudiante = models.CharField(max_length=20, unique=True)
    uid = models.CharField(max_length=255, blank=True, null=True, unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    balance = models.FloatField(default=0)
    Representative = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='numero_identidad')
    state = models.BooleanField(default=True)
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'ESTUDIANTE'
        verbose_name_plural = 'ESTUDIANTES'

