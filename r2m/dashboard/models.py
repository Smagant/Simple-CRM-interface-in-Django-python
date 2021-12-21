from django.db import models

class Client(models.Model):
    PROFESSION = (
        ('Avocat', 'Avocat'), 
        ('Expert-comptable', 'Expert-comptable'),
        ('Maire', 'Maire')
    )
    STATUT = (
        ('Client','Client'),
        ('Lead qualifié','Lead qualifié'),
        ('Prospect','Prospect')
    )
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    profession = models.CharField(max_length=200, null=True, blank=True, choices=PROFESSION)
    statut = models.CharField(max_length=200, null=True, blank=True, choices=STATUT)
    
    def __str__(self):
        return self.lastname

class ChefProjet(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.lastname

class Cadreur(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.lastname

class IngenieurSon(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.lastname

class Monteur(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.lastname

class Video(models.Model):
    PRODUCTION_STAGE = (
        ('En pré-production', 'En pré-production'),
        ('En production', 'En production'),
        ('En post-production', 'En post-production'),
        ('Publiée', 'Publiée')
    )
    LIEU_TOURNAGE = (
        ('Studio 1','Studio 1'),
        ('Studio 2','Studio 2'),
        ('Studio 3', 'Studio 3')
    )
    #Informations générales
    videoName = models.CharField(max_length=200, null=True, blank=True)
    stage = models.CharField(max_length=200, null=True, blank=True, choices=PRODUCTION_STAGE)
    datePublication = models.DateField(null=True, blank=True)
    lieuTournage = models.CharField(max_length=200, null=True, blank=True, choices=LIEU_TOURNAGE)
    dateTournage = models.DateField(null=True, blank=True)
    heureTournage = models.TimeField(null=True, blank=True)
    revenusGen = models.FloatField(null=True, blank=True)

    #Lien avec d'autres bases de données
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    chefProjet = models.ForeignKey(ChefProjet, null=True, blank=True, on_delete=models.SET_NULL)
    cadreur = models.ForeignKey(Cadreur, null=True, blank=True, on_delete=models.SET_NULL)
    ingénieurSon = models.ForeignKey(IngenieurSon, null=True, blank=True, on_delete=models.SET_NULL)
    monteur = models.ForeignKey(Monteur, null=True, blank=True, on_delete=models.SET_NULL)

    #Visibilité de la vidéo
    impressionsLinkedin = models.FloatField(null=True, blank=True)
    likesLinkedin = models.FloatField(null=True, blank=True)
    partagesLinkedin = models.FloatField(null=True, blank=True)

    impressionsFacebook = models.FloatField(null=True, blank=True)
    likesFacebook = models.FloatField(null=True, blank=True)
    partagesFacebook = models.FloatField(null=True, blank=True)

    impressionsInstagram = models.FloatField(null=True, blank=True)
    likesInstagram = models.FloatField(null=True, blank=True)
    partagesInstagram = models.FloatField(null=True, blank=True)

    impressionsTwitter = models.FloatField(null=True, blank=True)
    likesTwitter = models.FloatField(null=True, blank=True)
    partagesTwitter = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.videoName
