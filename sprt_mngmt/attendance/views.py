from django.shortcuts import render
from users import models

# Create your views here.
def attendance(request):
    player = "attendance not taken"

    if request.method == 'POST'
    player_att = Attendance(request.POST)

        if player_att.is_valid():
                player = player_att.clean_data['Attendance taken']
        else
            player_att = attendance
    return(render,'attendance')