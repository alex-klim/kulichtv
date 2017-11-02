from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, nickname, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not nickname:
            raise ValueError('The nickname must be set')
        user = self.model(nickname=nickname, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, nickname, password=None, **extra_fields):
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(nickname, password, **extra_fields)

    # def create_superuser(self, nickname, password, **extra_fields):
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self._create_user(nickname, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    nickname = models.CharField(max_length=50, unique=True, null=False)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'nickname'

    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
