from django import forms
from .models import Player_attendance

class Attendance(ModelForm):

    class Meta :
        model : Player_attendance
        fields : (
            'employee','attenance'
        )

AttendanceFormset = modelformset_factory(Attendance,fields=('attendance',)) 