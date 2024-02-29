from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('hello/',views.hello,name="hello"),
    path('contact/',views.contact,name="contact")
    
]
