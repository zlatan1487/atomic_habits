from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=140)
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE)

    def __str__(self):
        return self.username
