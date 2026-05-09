from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def listeProduits(request):
    produits = Produit.objects.all().order_by('nom')
    return render(request, 'stock/liste.html', {'produits': produits, 'total': produits.count()})


def ajouterProduits(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            nom_saisi = form.cleaned_data['nom']
            nouveau_prix = form.cleaned_data['prix_unitaire']
            quantite_ajoutee = form.cleaned_data['quantite']
            produit_existant = Produit.objects.filter(nom__iexact=nom_saisi).first()
            if produit_existant:
                produit_existant.quantite += quantite_ajoutee
                produit_existant.prix_unitaire = nouveau_prix
                produit_existant.save()
            else:
                form.save()
        return redirect('listeProduits')
    else:
        form = ProduitForm()
        return render(request, 'stock/ajouter.html', {'form': form})


def supprimerProduits(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('listeProduits')


def modifierProduits(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('listeProduits')
    else:
        form = ProduitForm(instance=produit)
        return render(request, 'stock/ajouter.html', {'form': form, 'modifier': True})