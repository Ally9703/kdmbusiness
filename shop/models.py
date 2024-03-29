from django.db import models
from django.contrib.auth.models import User 
#from django.utils import timezone


       
# Classe Client
class Client(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


# Classe Category
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


#Classe Produit   
class Produit(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='shop', null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)


    # Gestion d'affichage dans l'ordre d'ajout
    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name 
    
    # Ajout et gestion des produits sans images
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url             


# Classe commande 
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True) 
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)  

    # Savoir si nous avons au moins un produit physique
    @property
    def produit_physique(self):
        articlecommande = self.commandearticle_set.all()
        physique = any(article.produit.digital==False for article in articlecommande)
        return physique
    
        
    # Somme total des articles dans le panier
    @property 
    def get_panier_total(self):
        articles = self.commandearticle_set.all()
        total = sum(article.get_total for article in articles)
        return total  

    #Liste total des articles 
    @property
    def get_panier_article(self):
        articles = self.commandearticle_set.all()
        total = sum(article.quantite for article in articles)
        return total

class CommandeArticle(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # prix total des articles dans le panier
    @property
    def get_total(self):
        total = self.produit.price * self.quantite
        return total


class AddressChipping(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    addresse = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_ajout =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addresse