from django.shortcuts import render
from users.models import Profile
# Create your views here.

def att(request):
    context = {

        'players' : Profile.User

    }
    return render(request, 'attendance/staff.html', context)
    