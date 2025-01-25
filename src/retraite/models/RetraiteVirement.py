from django.db import models
from .Retraite import Retraite
from .Banque import Banque


class RetraiteVirement(models.Model):
    retraite = models.ForeignKey(Retraite, on_delete=models.SET_NULL, null=True)
    numero_RIB = models.CharField(max_length=150)
    modePaiement = models.CharField(max_length=10)
    echeancePremierVrmt = models.DateField()
    codeBanque = models.ForeignKey(Banque, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)