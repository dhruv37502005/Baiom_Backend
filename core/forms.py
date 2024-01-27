from django import forms
from .models import MaintenancePage

class AccessForm(forms.Form):
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter password'}),
        label=False
    )

class MaintenancePageForm(forms.ModelForm):
    class Meta:
        model = MaintenancePage
        fields = '__all__'
        widgets = {
            'end_time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }