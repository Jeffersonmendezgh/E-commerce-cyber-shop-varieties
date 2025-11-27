from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Modelo administrador de cuentas
class userManager(BaseUserManager):
    def create_user(self, email, name, lastname, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo")
        if not name:
            raise ValueError("El usuario debe tener un nombre")
        if not lastname:
            raise ValueError("El usuario debe tener apellido")
        if not username:
            raise ValueError("El usuario debe tener un username")
        
        user = self.model(
            name=name,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email),  # Convierte correo en minúscula y estándar
            **extra_fields  # Diccionario opcional con otros atributos
        )
        user.set_password(password)  # Hashea la contraseña
        user.save(using=self._db)  # Guarda el usuario en la base de datos
        return user
    
    def create_superuser(self, email, name, lastname, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superadmin', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser debe tener is_admin=True.')
        
        return self.create_user(email, name, lastname, username, password, **extra_fields)


class Auth(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)  # EmailField en lugar de CharField
    phone_number = models.CharField(max_length=12, blank=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_join = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # Cambiado a False por defecto
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'  # Para iniciar sesión
    REQUIRED_FIELDS = ['username', 'name', 'lastname']  # Campos obligatorios
    
    objects = userManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        """¿El usuario tiene un permiso específico?"""
        return self.is_admin
    
    def has_module_perms(self, app_label):
        """¿El usuario tiene permisos para ver la app `app_label`?"""
        return True
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'