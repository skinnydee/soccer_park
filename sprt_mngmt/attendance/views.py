from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Player_attendance
from django.views.generic.edit import View
from django.contrib.auth.models import User
# Create your views here

    
class attendance(View):
    template_name = 'attendace/staff.html'
    
    def get(self, request):
        context = {
            'players' : User.objects.all()
        }
        render(request, self.template_name, context)

    def post(self, request):
        
    