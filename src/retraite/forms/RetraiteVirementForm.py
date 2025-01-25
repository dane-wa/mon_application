from django import forms
from ..models import RetraiteVirement



class RetraiteVirementForm(forms.ModelForm):
    class Meta:
        model = RetraiteVirement
        fields = (

            'retraite',
            'numero_RIB',
            'modePaiement',
            'echeancePremierVrmt',
            'codeBanque',

        )

        widgets = {
            'codeBanque': forms.Select(attrs={'class': 'form-control'}),
            'retraite': forms.Select(attrs={'class': 'form-control'}),
            'numero_RIB': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de compte'}),
            'modePaiement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: VRMT pour (virement) ou TEL pour (téléphonie) '}),
            'echeancePremierVrmt': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'echeance de premier paiement au virement '}),
        }