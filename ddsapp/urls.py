from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', lambda request: render(request, 'success.html'), name='contact_success'),
]