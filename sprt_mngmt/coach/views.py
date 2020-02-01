from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def coach_register(request):
    form = UserCreationForm()
    return render(request, 'coach/register.html', {'form':form} )
