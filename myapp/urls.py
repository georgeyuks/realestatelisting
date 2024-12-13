
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('property/', views.property, name='property'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('book/', views.book, name='book'),
    path('message/', views.message, name='contact2'),
]
