from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import *
from .filters import VideoFilter
from .forms import VideoForm

# Create your views here.
def home(request): 
    context = {'title': 'test'}
    return render(request, 'dashboard/main.html', context)

def clientsBasePage(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'dashboard/clientsBasepage.html', context)

def clientPage(request, pk):
    client = Client.objects.get(id=pk)
    videos = client.video_set.all()
    videos_count = videos.count()
    myFilter = VideoFilter(request.GET, queryset=videos)
    videos = myFilter.qs

    context = {'client': client, 'videos':videos, 'videos_count':videos_count, 'myFilter': myFilter}
    return render(request, 'dashboard/client.html', context)

def videoBasePage(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'dashboard/videosBasepage.html', context)

def videoPage(request, pk):
    pass

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
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST',request.POST)
        #form = OrderForm(request.POST)
        formset = VideoFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}     
    return render(request, 'dashboard/video_form.html', context)


def updateVideo(request, pk):
    video = Video.objects.get(id=pk)
    form = VideoForm(instance=video)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'dashboard/video_form.html', context)

def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == "POST":
        video.delete()
        return redirect('/')
    context = {'item':video}
    return render(request, 'dashboard/delete.html', context)