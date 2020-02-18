
from django.contrib.auth.models import User
from django.shortcuts import render

def attendance(request):
    template_name = 'coach.attendance.html'
    player = filter(User.objects.na)
    return render(request,'coach/attendance.html', {'players' : player})