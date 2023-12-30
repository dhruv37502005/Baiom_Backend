from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
        
    class Meta(AbstractUser.Meta):
        pass


User._meta.get_field('groups').related_name = 'userauths_groups'
User._meta.get_field('user_permissions').related_name = 'userauths_user_permissions'