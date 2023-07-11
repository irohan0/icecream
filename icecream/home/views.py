from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def mailsender(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        
        msg = request.POST.get('message')
        print(sub,msg)
        
        send_mail(
            sub,msg,'mtest01311@gmail.com',
            ['rohan.inamdar222@gmail.com','kavin.sundarr@gmail.com']
        )
        HttpResponse(" Mail Sent !")
        messages.success(request, 'Your message has been sent!')
    return render(request,'mailsender.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        Contact = contact(name=name, email=email, phone=phone, desc=desc, date = date)

        Contact.save()
        #messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
