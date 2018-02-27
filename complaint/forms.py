from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        labels = {
            'state': _('Estado'),
            'type': _('Tipo'),
            'sex': _('Sexo'),
            'injured': _('¿Está Herido?'),
            'place': _('Lugar')
        }
        widgets = {
            'state': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'injured:': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'})
        }

