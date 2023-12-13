from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=50, unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  def _str_(self):
    return self.username
  
    

# Create your models here.
