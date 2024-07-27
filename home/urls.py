from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path("employee", views.index, name='index'),
    path("all", views.all, name='all'),
    path("remove", views.remove, name='remove'),
    path("remove_emp/<int:id_no>", views.remove, name='remove'),
    path("filter", views.filter, name='filter'),
]
