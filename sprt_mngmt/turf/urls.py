
from django.urls import path
from . import views
from sprt_mngmt import urls

urlpatterns =[
    path('',views.home, name = 'turf-home'),
    path('about/',views.about, name = 'turf-about'),
]