from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UseRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', ]

    def clean(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        name = self.cleaned_data.get("username")
        if pass1 != pass2:
            raise forms.ValidationError("password must be equal to confirm password")
        elif len(name) <= 4:
            raise forms.ValidationError("Name must be greater than 4 chars")
        return cleaned_data
