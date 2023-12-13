from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
class Useregisterform(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','email',]
        
