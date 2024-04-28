"""
Database model
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManage(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_field):
        """Create Save and Return a new user"""
        if not email:
            raise ValueError("User most have an Email addresse")
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Create super User"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        return user

    
class User(AbstractBaseUser, PermissionsMixin):
    """ User in the systeme"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=2500)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManage()

    USERNAME_FIELD = 'email'
