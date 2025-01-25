from django.db import models

class Employeur(models.Model):
    codeEmployeur = models.CharField(max_length=10)
    nomEmployeur = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomEmployeur}"
