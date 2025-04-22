from django.shortcuts import redirect,render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User



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

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=user_id)

            if has_contacted:
                messages.error(request,'You already sent a message .Our team will contact  you soon ')
                return redirect('/cars/'+car_id)
           
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)

        admin_info=User.objects.get(is_superuser=True)
        admin_email=admin_info.email

        send_mail(
            "New  Car Inquiry ",
            "You have been new inquiry for" +car_title+".please login to get more info",
            "alvinantony2112@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request,'Your message submitted ')
        return redirect('/cars/'+car_id)
    
    



