
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Ice-Cream Factory Admin"
admin.site.site_title = "Ice-Cream Factory Admin Portal"
admin.site.index_title = "Welcome to Ice-Cream Factory"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    
]
