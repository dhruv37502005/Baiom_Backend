from django import forms
from .models import DashboardUser

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = DashboardUser
        fields = "__all__"