from django.contrib import admin
from django.urls import path
from mailsender import views

urlpatterns = [
    path("/mailsender",views.mailsender,name='mailsender')
]
