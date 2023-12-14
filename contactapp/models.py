from django.db import models


class contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=13)
    phone = models.CharField(max_length=100)
    content = models.TextField()

# Create your models here.

# Create your models here.

# Create your models here.
