from django.urls import path
from django.contrib import admin
from home_com import views

urlpatterns = [
    path("", views.C_home, name='C_home'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("job", views.job, name='job'),
]