from django.db import models
from .Retraite import Retraite
from .Prefecture import Prefecture

class RetraiteDeces(models.Model):
    retraite =models.ForeignKey(Retraite, on_delete=models.SET_NULL, null=True)
    dateDeces = models.DateField()
    dateDeclaration = models.DateField()
    AssignationDefunt = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)