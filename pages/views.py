from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all() #整個Teams的資料 queryset
    # 資料要是字典{ }
    data = {
        'teams': teams
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all() 
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def campervans(request):
    return render(request, 'pages/campervans.html')