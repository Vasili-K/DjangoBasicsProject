from django.shortcuts import render

# Create your views here.


def weather_home(request):
    return render(request, 'weather/weather_home.html')
