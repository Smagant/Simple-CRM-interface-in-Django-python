from django.shortcuts import render

# Create your views here.
def home(request): 
    context = {'title': 'test'}
    return render(request, 'dashboard/main.html', context)