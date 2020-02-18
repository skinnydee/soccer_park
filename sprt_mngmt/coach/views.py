from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CoachRegisterForm

# Create your views here.
def coach_register(request):
    if request.method == 'POST':
        form = CoachRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('id_username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('coach_login')
    else:
        form = CoachRegisterForm(request.GET)
    return render(request, 'coach/register.html', {'form':form} )
