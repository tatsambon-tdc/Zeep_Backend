"""
Nos Models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """La classe pour gerer le model User"""
    def create_user(self, email, password=None, **extrafield):
        """Creation et renvoi du nouvau User"""
        if not email:
            raise ValueError('L\'user doit avoir une Email')
        user = self.model(email=self.normalize_email(email), **extrafield)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creation et renvoi du nouveau ***SuperUser*** """

        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """La classe user de notre sys"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
