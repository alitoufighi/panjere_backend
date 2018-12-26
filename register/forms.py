from django import forms
from .models import Attendant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendant
        fields = ('first_name', 'last_name', 'email', 'major', 'university')
