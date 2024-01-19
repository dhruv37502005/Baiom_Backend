from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from datetime import date

from course.models import Course

# Create your models here.


#user = models.OneToOneField(settings.AUTH_USER_MODEL)

class Dashboard_User(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_user = models.BooleanField(default=True)
    
    is_employee = models.BooleanField(default=False)

    bio = models.CharField(max_length=100, blank=True)
    fname = models.CharField(max_length=30, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    mname = models.CharField(max_length=30, blank=True)
    mobilenumber = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    collegename = models.CharField(max_length=100, blank=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    current_designation = models.CharField(max_length=50, blank=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='enrolled_users', blank=True)


    def __str__(self):
        return self.user.username

    

   

    
# class Employee(models.Model):
#      user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#      is_user = models.BooleanField(default=False)   
#      is_employee = models.BooleanField(default=True)
#      bio = models.CharField(max_length=100, blank=True)
#      fname = models.CharField(max_length=30, blank=True)
#      lname = models.CharField(max_length=30, blank=True)
#      mname = models.CharField(max_length=30, blank=True)
#      mobilenumber = models.CharField(max_length=15, blank=True)
#      photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
#      designation = models.CharField(max_length=30, blank=True)

#      def __str__(self):
#          return self.user.username