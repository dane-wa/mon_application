from django.db import models
from django.db.models import Q, When, Case
from .Prefecture import Prefecture
from .Employeur import Employeur




class Retraite(models.Model):
    TITLE_TYPE = (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),
    )

    RETRAITE_TYPE = (
        ('01-', 'Retraite'),
    )

    nPension = models.IntegerField(unique=True, blank=False)
    titre = models.CharField(max_length=3, choices=TITLE_TYPE)
    employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=RETRAITE_TYPE)
    dateNais = models.DateField()
    dateJouis = models.DateField()
    montantTrim = models.FloatField(blank=True, null=True)
    allocation = models.FloatField(blank=True, null=True)
    MensuelDu = models.FloatField(blank=True, null=True, default=0)
    montantTotal = models.FloatField(blank=True, null=True)
    montantTrim_40 = models.FloatField(blank=True, null=True)
    montantComp = models.FloatField(blank=True, null=True)
    Observation = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='retraites_images/%Y/%m/%d/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def montantMensuel(self):
        if 264000.00 <= self.montantTrim_40 <= 616000.00:
            return self.montantTrim_40 * 2.2 / 3
        elif 616000.00 < self.montantTrim_40 <= 1537099.00:
            return self.montantTrim_40 * 1.85 / 3
        elif self.montantTrim_40 > 1537099.00:
            return self.montantTrim_40 * 1.5 / 3
        return 0

    def montantPaye(self):
        return (self.MensuelDu + 1)* self.montantMensuel() + self.montantComp


    def __str__(self):
        return f"{self.nPension}"