
from django.contrib.auth.models import User
from django.shortcuts import render

def attendance(request):
    template_name = 'coach.attendance.html'
    players = User.objects.all()
    context = {
        "players" : players
    }
    return render(request,'coach/attendance.html', context)

