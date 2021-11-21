from django.shortcuts import render
from .models import *


# Create your views here.
def home(request): 
    context = {'title': 'test'}
    return render(request, 'dashboard/main.html', context)

def clientsBasePage(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'dashboard/clientsBasepage.html', context)

def clientPage(request, pk):
    pass

def videoBasePage(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'dashboard/videosBasepage.html', context)

def videoPage(request, pk):
    pass


