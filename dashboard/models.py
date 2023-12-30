from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser, Group ,Permission

class DashboardUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=100, blank=True)
    fname = models.CharField(max_length=30, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    mname = models.CharField(max_length=30, blank=True)
    mobilenumber = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    collegename = models.CharField(max_length=100, blank=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    current_designation = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
        
    class Meta(AbstractUser.Meta):
        pass

DashboardUser._meta.get_field('groups').related_name = 'dashboard_groups'
DashboardUser._meta.get_field('user_permissions').related_name = 'dashboard_user_permissions'

# class DashboardGroup(Group):
#     class Meta:
#         proxy=True
# class DashboardPermission(Permission):
#     class Meta:
#         proxy=True
    