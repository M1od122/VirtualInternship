from django import forms
from .models import MountainPass

class MountainPassForm(forms.ModelForm):
    class Meta:
        model = MountainPass  # Указываем модель, которую будем использовать
        fields = ['name', 'email', 'phone_number', 'address']