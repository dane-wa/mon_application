from django import forms
from ..models import Employeur



class EmployeurForm(forms.ModelForm):
    class Meta:
        model = Employeur
        fields = (

            'codeEmployeur',
            'nomEmployeur',
        )

        widgets = {
            'codeEmployeur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro Employeur'}),
            'nomEmployeur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la Société'}),
        }