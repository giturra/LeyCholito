from django import forms
from .models import NaturalPerson


class RegisterNaturalUserForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = '__all__'


class LogInForm(forms.Form):
    username = forms.CharField(label='Nombre: ', max_length=200)