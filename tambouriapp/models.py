from django.db import models

# Create your models here.

class Voiture(models.Model):
    #modele
    modele = models.CharField(max_length=100)
    #marque
    marque = models.CharField(max_length=100)
    #annee
    annee = models.DateTimeField()
    #photo
    photo = models.ImageField()
    #description
    description = models.TextField()
    #prix de vente
    prix_vente = models.IntegerField()
    #vendu
    vendu = models.BooleanField(default="False")
    #quantite
    quantite = models.IntegerField()

    class Meta():
        verbose_name = 'Voiture'
        verbose_name_plural = 'Voitures'

    def __str__(self):
        return self.marque


class Villa(models.Model):
    #localisation
    #numero
    numero = models.IntegerField()
    #description TextField
    description = models.TextField()
    #photo ImageField
    photo = models.ImageField()
    #prix de vente IntegerField
    prix_vente = models.IntegerField()
    #vendu
    vendu = models.BooleanField(default="False")
    #quantite
    quantite = models.IntegerField()

    def __str__(self):
        return self.numero

class Peintre(models.Model):
    #nom
    nom = models.CharField(max_length = 100)
    #prenom
    prenom = models.CharField(max_length = 100)
    #surnom ou nom d'artiste
    surnom = models.CharField(max_length = 100)

    def __str__(self):
        return self.surnom

class Tableau(models.Model):
    #prix
    #peintre
    peintre = models.ForeignKey(Peintre)
    #nom
    nom = models.CharField(max_length = 200)
    #quantite
    photo = models.ImageField()
    #description
    description = models.TextField()
    #prix de vente
    prix_vente = models.IntegerField()
    #vendu
    vendu = models.BooleanField(default="False")
    #quantite
    quantite = models.IntegerField()

    class Meta():
        verbose_name = 'Tableau'
        verbose_name_plural = 'Tableaux'

    def __str__(self):
        return self.nom
