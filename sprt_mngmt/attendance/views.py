from django.shortcuts import render
from users.models import User
# Create your views here.

def att(request):
    context = {

        'player' : User.username

    }
    return(request, 'attendance/staff.html')
    