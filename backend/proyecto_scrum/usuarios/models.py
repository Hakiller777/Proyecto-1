from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario debe tener is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

class Usuario(models.Model):
    # Campos personalizados para tu modelo de usuario
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Almacenamiento de contraseñas
    # ... otros campos

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    # Métodos para la gestión de usuarios
    def has_perm(self, perm, obj=None):
        # Verifica si el usuario es superusuario
        if self.is_superuser:
            return True

        # Verifica si el usuario tiene el permiso específico
        return self.user_permissions.filter(codename=perm).exists()

    def has_perms(self, perm_list, obj=None):
        # Verifica si el usuario es superusuario
        if self.is_superuser:
            return True

        # Verifica si el usuario tiene todos los permisos de la lista
        for perm in perm_list:
            if not self.user_permissions.filter(codename=perm).exists():
                return False
        return True

    def has_module_perms(self, app_label):
        # Verifica si el usuario es superusuario
        if self.is_superuser:
            return True

        # Verifica si el usuario tiene permisos para el módulo
        return self.user_permissions.filter(content_type__app_label=app_label).exists()

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True, verbose_name=_('groups'))
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True, verbose_name=_('user permissions'))

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: All superusers have all permissions.
        if self.is_superuser:
            return True
        return self.user_permissions.filter(codename=perm).exists()

    def has_perms(self, perm_list, obj=None):
        "Does the user have all permissions?"
        # Simplest possible answer: All superusers have all permissions.
        if self.is_superuser:
            return True
        return all(self.user_permissions.filter(codename=perm).exists() for perm in perm_list)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: All superusers have all permissions.
        if self.is_superuser:
            return True
        return bool(self.user_permissions.filter(content_type__app_label=app_label).exists())

    def get_username(self):
        return self.username

class UserProfile(Usuario, PermissionsMixin):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profile_set',  # Nombre único para el acceso inverso
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profile_set',  # Nombre único para el acceso inverso
        blank=True,
        verbose_name='user permissions',
    )
