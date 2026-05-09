from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.listeProduits, name='listeProduits'),
    path('ajouter/', views.ajouterProduits, name='ajouterProduits'),
    path('supprimer/<int:pk>/', views.supprimerProduits, name='supprimerProduits'),
    path('modifier/<int:pk>/', views.modifierProduits, name='modifierProduits'),
]
