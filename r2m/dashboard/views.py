from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import VideoForm, ClientForm


#Fonction pour la page d'accueil contenant le dashboard
def home(request):
    clients = Client.objects.all()
    videos = Video.objects.all()
    
    #Calculer le chiffre d'affaires et le coût total total généré sur l'ensemble des vidéos
    totalRev = 0
    totalCost = 0
    for v in videos:
        try:
            totalCost += v.chefProjet.cost + v.cadreur.cost + v.ingénieurSon.cost + v.monteur.cost
            totalRev += v.revenusGen
        except:
            continue

    grossMarginPercent = round(((totalRev - totalCost)/totalRev)*100)
    grossMarginValue = totalRev - totalCost
    
    #Nombre total d'individus dans la base de données
    nbIndiv = clients.count()

    #Nombre total d'individus ayant le statut de clients
    nbClients = 0
    for i in clients:
        try:
            if i.statut == 'Client':
                nbClients += 1
                continue
        except:
            continue
    
    #Nombre total d'individus ayant le statut de leads qualifiés
    nbLeads = 0
    for i in clients:
        try:
            if i.statut == 'Lead qualifié':
                nbLeads += 1
                continue
        except:
            continue
    
    #Nombre total d'individus ayant le statut de prospects
    nbProspects = 0
    for i in clients:
        try:
            if i.statut == 'Prospect':
                nbProspects += 1
                continue
        except:
            continue
    
    #Nombre total d'individus ayant pour profession : avocat
    nbAvocats = 0
    for i in clients:
        try:
            if i.profession == 'Avocat':
                nbAvocats += 1
                continue
        except:
            continue
    
    #Nombre total d'individus ayant pour profession : maire
    nbMaires = 0
    for i in clients:
        try:
            if i.profession == 'Maire':
                nbMaires += 1
                continue
        except:
            continue
    
    #Nombre total d'individus ayant pour profession : expert-comptable
    nbExpCompt = 0
    for i in clients:
        try:
            if i.profession == 'Expert-comptable':
                nbExpCompt += 1
                continue
        except:
            continue

    #Taux de conversion client
    conversionRate = round((nbClients/nbIndiv)*100)
    
    context = {
        'totalRev':totalRev,
        'totalCost':totalCost,
        'grossMarginValue':grossMarginValue,
        'grossMarginPercent':grossMarginPercent,
        'nbIndiv':nbIndiv,
        'nbClients':nbClients,
        'nbLeads':nbLeads,
        'nbProspects':nbProspects,
        'nbAvocats':nbAvocats,
        'nbMaires':nbMaires,
        'nbExpCompt':nbExpCompt,
        'conversionRate':conversionRate
    }
    return render(request, 'dashboard/dashboardPage.html', context)

#Fonction pour la page de listing des clients
def clientsBasePage(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'dashboard/clientsBasepage.html', context)

#Fonction pour la page spécifique de chaque client
def clientPage(request, pk):
    #Récupérer les informations du client
    client = Client.objects.get(id=pk)
    #Récupérer les informations sur les vidéos du client spécifiquement
    videos = client.video_set.all()
    #Compter le nombre de vidéo qu'à fait le client au total
    videos_count = videos.count()
    #Calculer le coût de toutes les vidéos du client
    clientCost = 0
    for v in videos:
        try:
            clientCost += v.chefProjet.cost + v.cadreur.cost + v.ingénieurSon.cost + v.monteur.cost
        except:
            continue
    #Calculer le revenus de toutes les vidéos du client
    clientRev = 0
    for v in videos:
        try:
            clientRev += v.revenusGen
        except:
            continue
    context = {'client': client, 'videos':videos, 'videos_count':videos_count, 'clientCost': clientCost, 'clientRev':clientRev}
    return render(request, 'dashboard/client.html', context)

#Fonction pour la page de listing de toutes les vidéos
def videoBasePage(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'dashboard/videosBasepage.html', context)

#Fonction pour la page spécifique pour chaque vidéo
def videoPage(request, pk):
    video = Video.objects.get(id=pk)
    cost = video.chefProjet.cost + video.cadreur.cost + video.ingénieurSon.cost + video.monteur.cost
    context = {'video':video, 'cost':cost}
    return render(request, 'dashboard/video.html', context)

#Fonction pour créer un client 
def createClient(request):
	form = ClientForm()
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'dashboard/client_form.html', context)

#Fonction pour modifier un client
def updateClient(request, pk):
	client = Client.objects.get(id=pk)
	form = ClientForm(instance=client)

	if request.method == 'POST':
		form = ClientForm(request.POST, instance=client)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'dashboard/client_updateForm.html', context)

#Fonction pour supprimer un client
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect('/')
    context = {'item':client}
    return render(request, 'dashboard/deleteClient.html', context)


#Fonction pour créer une vidéo
def createVideo(request, pk):
    videoFields = (
        'videoName',
        'stage',
        'datePublication',
        'lieuTournage',
        'dateTournage',
        'heureTournage',
        'revenusGen',
        'chefProjet',
        'cadreur',
        'ingénieurSon',
        'monteur',
        'impressionsLinkedin',
        'likesLinkedin',
        'partagesLinkedin',
        'impressionsFacebook',
        'likesFacebook',
        'partagesFacebook',
        'impressionsInstagram',
        'likesInstagram',
        'partagesInstagram',
        'impressionsTwitter',
        'likesTwitter',
        'partagesTwitter'
    )
    
    VideoFormSet = inlineformset_factory(Client, Video, fields=videoFields, extra=1)
    client = Client.objects.get(id=pk)
    formset = VideoFormSet(queryset=Video.objects.none(), instance=client)
    if request.method == 'POST':
        formset = VideoFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}     
    return render(request, 'dashboard/video_form.html', context)

#Fonction pour mettre à jour une vidéo
def updateVideo(request, pk):
	video = Video.objects.get(id=pk)
	form = VideoForm(instance=video)

	if request.method == 'POST':
		form = VideoForm(request.POST, instance=video)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'dashboard/video_updateForm.html', context)

#Fonction pour supprimer une vidéo
def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == "POST":
        video.delete()
        return redirect('/')
    context = {'item':video}
    return render(request, 'dashboard/deleteVideo.html', context)