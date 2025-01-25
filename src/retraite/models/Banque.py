from django.db import models

class Banque(models.Model):
    codeBanque = models.CharField(max_length=10)
    libelle = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.libelle}"