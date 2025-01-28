from django.contrib import admin
from .models.Retraite import Retraite, Prefecture, Employeur
from django.utils.html import format_html
from .models.Banque import Banque
from .models.RetraiteDeces import RetraiteDeces
from .models.EcheancesRetraite import EcheancesRetraite
from .models.RetraiteVirement import RetraiteVirement


class RetraiteAdmin(admin.ModelAdmin):

    list_display = (
        'nPension',
        'prenom',
        'nom',
        'dateNais',
        'dateJouis',
        'montantTrim_40',
        'montantMensuel',
        'montantComp',
        'Observation',
        'image',

    )
    list_display_links = ('nPension',)
    list_per_page = 10




class PrefectureAdmin(admin.ModelAdmin):
    list_display = (
        'codePrefecture',
        'nomPrefecture',
    )
    list_display_links = ('codePrefecture',)
    list_per_page = 10


class EmployeurAdmin(admin.ModelAdmin):
    list_display = (
        'codeEmployeur',
        'nomEmployeur',
    )
    list_display_links = ('codeEmployeur',)
    list_per_page = 10


class EcheancesRetraiteAdmin(admin.ModelAdmin):
    list_display = (
        'dateecheance',
    )


admin.site.register(Retraite, RetraiteAdmin)
admin.site.register(Employeur, EmployeurAdmin)
admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Banque)
admin.site.register(RetraiteVirement)
admin.site.register(RetraiteDeces)
admin.site.register(EcheancesRetraite)

