from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def att(request):
    context = {
        'players' : User.objects.all()
    }
    return render(request, 'attendance/staff.html', context)
    