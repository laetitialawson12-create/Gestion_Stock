from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantite = models.PositiveIntegerField(default=0)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nom} - {self.quantite} en stock"
    
    def calculer_total(self):
        return self.quantite * self.prix_unitaire