
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name = 'turf-home'),
    path('about/',views.about, name = 'turf-about'),
]