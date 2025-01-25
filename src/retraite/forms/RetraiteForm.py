from django import forms
from ..models import Retraite



class RetraiteForm(forms.ModelForm):
    class Meta:
        model = Retraite
        fields = (

            'titre',
            'type',
            'nPension',
            'prenom',
            'nom',
            'dateNais',
            'dateJouis',
            'employeur',
            'prefecture',
            'montantTrim',
            'allocation',
            'MensuelDu',
            'montantTotal',
            'montantTrim_40',
            'montantComp',
            'image',
            'Observation',
        )

        widgets = {
            'nPension': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de Pension'}),
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mr/Mme'}),
            'employeur': forms.Select(attrs={'class': 'form-control'}),
            'prefecture': forms.Select(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s) Retraite'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Retraite'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'dateNais': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de Naissance'}),
            'dateJouis': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de Jouissance'}),
            'montantTrim': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant Trimestriel'}),
            'allocation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Allocation'}),
            'MensuelDu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mensuel Dû(s)'}),
            'montantTotal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant Trimestriel Total'}),
            'montantTrim_40': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant Trimestriel Revalorisé 40 %'}),
            'montantComp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant Complémentaire'}),
            'Observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Texte', 'rows': 2, 'cols': 20}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }