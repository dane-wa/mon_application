from django.db import models



class Prefecture(models.Model):
    codePrefecture = models.CharField(max_length=10)
    nomPrefecture = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomPrefecture}"