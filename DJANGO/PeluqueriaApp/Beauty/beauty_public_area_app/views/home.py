from django.shortcuts import render


def beauty_public_home(request):
    return render(request, 'public_area/home/home.html')