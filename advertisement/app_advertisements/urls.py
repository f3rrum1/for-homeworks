from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path('', index, name= 'index'),
    path('top-sellers', topSellers, name= 'top-sellers'),
]