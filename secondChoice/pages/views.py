from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.db.models.functions import Lower


# Create your views here.

def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
    # search_fields=Car.objects.values('model','city','year','body_style','price')
    search_model=Car.objects.values_list('model',flat=True).distinct()
    search_city=Car.objects.values_list('city',flat='True').distinct()
    search_year=Car.objects.values_list('year',flat=True).distinct()
    search_body_style=Car.objects.annotate(body_style_lower=Lower('body_style')).values_list('body_style_lower',flat=True).distinct()



    data={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'search_model':search_model,
        'search_city':search_city,
        'search_year':search_year,
        'search_body_style':search_body_style,
        



    }
    return render(request,'pages/home.html',data)
def cars(request):
    
    return render(request,'cars/cars.html')

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')


def contact(request):
    return render(request,'pages/contact.html')
