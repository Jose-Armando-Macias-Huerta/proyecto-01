from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    RFC = models.CharField(max_length=13, blank=True)
    NombreCompleto = models.CharField(max_length=50)
    CURP = models.CharField(max_length=18, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email