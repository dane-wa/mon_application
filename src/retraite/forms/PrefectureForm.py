from django import forms
from ..models import Prefecture



class PrefectureForm(forms.ModelForm):
    class Meta:
        model = Prefecture
        fields = (

            'codePrefecture',
            'nomPrefecture',
        )

        widgets = {
            'codePrefecture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro Assignation'}),
            'nomPrefecture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Préfecture'}),
        }