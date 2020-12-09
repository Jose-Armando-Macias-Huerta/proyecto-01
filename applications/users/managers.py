from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password,is_superuser, **extra_fields):
        user = self.model(
            email=email,
            password=password,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password,**extra_fields):
        return self._create_user(email, password, True, **extra_fields)
