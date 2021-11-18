from django.db import models

class Client(models.Model):
    PROFESSION = ('Avocat', 'Expert-comptable', 'Maire')
    STATUT = ('Client', 'Lead qualifié', 'Prospect')
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    profession = models.CharField(max_length=200, null=True, choices=PROFESSION)
    statut = models.CharField(max_length=200, null=True, choices=STATUT)
    
    def __str__(self):
        return [self.firstname, self.lastname]

class ChefProjet(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    
    def __str__(self):
        return [self.firstname, self.lastname]

class Cadreur(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    
    def __str__(self):
        return [self.firstname, self.lastname]


class IngénieurSon(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return [self.firstname, self.lastname]

class Monteur(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return [self.firstname, self.lastname]

class Video(models.Model):
    PRODUCTION_STAGE = ('En pré-production', 'En production', 'En post-production', 'Publiée')
    LIEU_TOURNAGE = ('Studio 1', 'Studio 2', 'Studio 3')
    #Informations générales
    videoName = models.CharField(max_length=200, null=True)
    stage = models.CharField(max_length=200, null=True, choices=PRODUCTION_STAGE)
    datePublication = models.DateField(null=True)
    lieuTournage = models.CharField(max_length=200, null=True, choices=LIEU_TOURNAGE)
    dateTournage = models.DateField(null=True)
    heureTournage = models.TimeField(null=True)
    revenusGen = models.FloatField(null=True)

    #Lien avec d'autres bases de données
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    chefProjet = models.ForeignKey(ChefProjet, null=True, on_delete=models.SET_NULL)
    cadreur = models.ForeignKey(Cadreur, null=True, on_delete=models.SET_NULL)
    ingénieurSon = models.ForeignKey(IngénieurSon, null=True, on_delete=models.SET_NULL)
    monteur = models.ForeignKey(Monteur, null=True, on_delete=models.SET_NULL)

    #Visibilité de la vidéo
    impressionsLinkedin = models.FloatField(null=True)
    likesLinkedin = models.FloatField(null=True)
    partagesLinkedin = models.FloatField(null=True)

    impressionsFacebook = models.FloatField(null=True)
    likesFacebook = models.FloatField(null=True)
    partagesFacebook = models.FloatField(null=True)

    impressionsInstagram = models.FloatField(null=True)
    likesInstagram = models.FloatField(null=True)
    partagesInstagram = models.FloatField(null=True)

    impressionsTwitter = models.FloatField(null=True)
    likesTwitter = models.FloatField(null=True)
    partagesTwitter = models.FloatField(null=True)

    def __str__(self):
        return self.videoName
