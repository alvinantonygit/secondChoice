from django.shortcuts import redirect,render
from .models import Contact
from django.contrib import messages



# Create your views here.
def inquiry(request):
    if request.method=='POST':

        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        customer_need=request.POST.get('customer_need')
        user_id=request.POST.get('user_id')
        car_title=request.POST.get('car_title')
        city=request.POST.get('city')
        email=request.POST.get('email')
        state=request.POST.get('state')
        message=request.POST.get('message')
        car_id=request.POST.get('car_id')
        phone=request.POST.get('phone')


        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)

        contact.save()
        messages.success(request,'Your message submitted ')
        return redirect('/cars/'+car_id)
    
    



