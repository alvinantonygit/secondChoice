from django.shortcuts import render

# Create your views here.
def Cars(request):
    return render(request,'cars/cars.html')