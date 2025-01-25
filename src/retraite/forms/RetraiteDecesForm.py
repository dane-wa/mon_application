from django import forms
from ..models import RetraiteDeces



class RetraiteDecesForm(forms.ModelForm):
    class Meta:
        model = RetraiteDeces
        fields = (

            'retraite',
            'dateDeces',
            'AssignationDefunt',
            'dateDeclaration',

        )

        widgets = {
            'AssignationDefunt': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assignation du defunt'}),
            'retraite': forms.Select(attrs={'class': 'form-control'}),
            'dateDeces': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de Décès'}),
            'dateDeclaration': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de déclaration à la CNSS'}),
        }