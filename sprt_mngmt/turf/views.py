from django.shortcuts import render, redirect
from .calendar_app import Cal


def home(request):
    return render(request,'turf/home.html')

def about(request):
    return render(request,'turf/about.html')

def calendar(request):
    if request.method == 'POST':
        form = Cal(request.POST)
        if form.is_valid():
            description = form.clean_data.get('description')
    else:
        form = Cal()
    return render(request,'turf/calapp.html',{'form':form})

def logout(request):
    auth.logout(request);
    return redirect('/')
    