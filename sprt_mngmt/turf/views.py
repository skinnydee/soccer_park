from django.shortcuts import render

players = [

    {
        'Name' : 'Nixon',
        'Rank' : '11',
        'position' : 'mid fielder'
    },
    {
        'Name' : 'Cristin',
        'Rank' : '12',
        'position' : 'Goalee'
    }

]

def home(request):
    context = {
        'team':players
    }
    return render(request,'turf/home.html', context)

def about(request):
    return render(request,'turf/about.html')

