from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name='About'),
    path("menu",views.services,name='Services'),
    path("contact",views.contact,name='Contact'),
    path("mailsender",views.mailsender,name='Mailsender')
    #path('mailsender',include('mailsender.urls'))
]
