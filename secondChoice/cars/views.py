from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower


# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 5)  # Fixed: capital 'P' for Paginator
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)  # Fixed: correct method
    search_model=Car.objects.values_list('model',flat=True).distinct()
    search_city=Car.objects.values_list('city',flat='True').distinct()
    search_year=Car.objects.values_list('year',flat=True).distinct()
    search_body_style=Car.objects.annotate(body_style_lower=Lower('body_style')).values_list('body_style_lower',flat=True).distinct()

    data = {
        'cars': paged_cars,
        'search_model':search_model,
        'search_city':search_city,
        'search_year':search_year,
        'search_body_style':search_body_style,
        
    }

    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):

    search_model=Car.objects.values_list('model',flat=True).distinct()
    search_city=Car.objects.values_list('city',flat='True').distinct()
    search_year=Car.objects.values_list('year',flat=True).distinct()
    search_body_style=Car.objects.annotate(body_style_lower=Lower('body_style')).values_list('body_style_lower',flat=True).distinct()
    search_transmission=Car.objects.values_list('transmission',flat=True).distinct()


    car=Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']

        if keyword:
            car=car.filter(description__icontains=keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model and model.lower() != 'select model':
            car = car.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city and city.lower() != 'city':
            car = car.filter(city__iexact=city)
    if 'year' in request.GET:
        year = request.GET['year']
        if year and year.lower() != 'year':
            car = car.filter(model__iexact=year)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if model and model.lower()  != 'body type':
            car = car.filter(model__iexact=body_style)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']

        if max_price:
            car=car.filter(price__gte=min_price,price__lte=max_price)

    

    data= {
        'cars':car,
        'search_model':search_model,
        'search_city':search_city,
        'search_year':search_year,
        'search_body_style':search_body_style,
        'search_transmission':search_transmission,
    }
    return render(request, 'cars/search.html',data)  # Fixed: file extension
