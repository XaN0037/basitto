from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from rest_framework.authentication import TokenAuthentication


class CustomUserManager(BaseUserManager):

    def create_user(self, mobile, password, **extra_fields):
        mobile = mobile
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(mobile, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=254, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(("password"), max_length=128)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    authentication_classess = (TokenAuthentication,)
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.mobile},{self.name}"


class ServerTokens(models.Model):
    key = models.CharField(max_length=256)
    token = models.CharField(max_length=2000)

    def __str__(self):
        return self.key


class OTP(models.Model):
    key = models.CharField(max_length=256)
    mobile = models.CharField(max_length=25)
    tries = models.IntegerField(default=0)
    is_expired = models.BooleanField(default=False)
    state = models.CharField(max_length=128, default="step_one")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
