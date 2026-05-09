from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        # On dit à Django quels champs afficher dans le formulaire
        fields = ['nom', 'description', 'quantite', 'prix_unitaire']
        
        # On ajoute du style Bootstrap aux cases de saisie
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
        }