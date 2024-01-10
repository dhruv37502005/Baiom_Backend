from django import forms
from userauths.models import Dashboard_User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Dashboard_User
        fields = ['bio', 'fname', 'lname', 'mname', 'mobilenumber', 'photo', 'collegename', 'graduation_year', 'current_designation']
        