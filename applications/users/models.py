from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class usuario(AbstractBaseUser, PermissionsMixin):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    email = models.EmailField(max_length=30, blank=True, unique=True)
    RFC = models.CharField(max_length=18, blank=True)
    username = models.CharField(max_length=50, unique=True)
    CURP = models.CharField(max_length=18, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id']

    objects = UserManager()

    def __str__(self):
        return self.email