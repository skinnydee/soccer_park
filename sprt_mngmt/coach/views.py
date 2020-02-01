from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from .regforms import CoachForm

# Create your views here.
def coach_register(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('cooach_login')
    else:
        form = CoachForm()
    return render(request, 'coach/register.html', {'form':form} )
