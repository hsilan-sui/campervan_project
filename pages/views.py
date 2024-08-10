from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all() #整個Teams的資料 queryset

    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)

    all_cars = Car.objects.order_by('-created_date')
    #搜尋表單的欄位 要改車款(幾人座)
    search_fields = Car.objects.values('model','city','year','body_style')
    # 資料要是字典{ }
    data = {
        'teams': teams,
        'featured_car': featured_car,
        'all_cars': all_cars,
        'search_fields': search_fields
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