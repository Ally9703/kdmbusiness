from django.urls import path 
from . import views

app_name = "shop"

urlpatterns = [

    path('', views.shop, name='shop'),
    path('produit/', views.produit, name="produit" ),
    path('panier/', views.panier, name="panier" ),
    path('commande/', views.commande, name="commande"),
    path('about/', views.about, name="about"),
    path('question/', views.question, name="question"),
    path('update_article/', views.update_article, name='update_article'),
    path('traitement_commande/', views.traitement_commande, name="traitement_commande"),
   
]