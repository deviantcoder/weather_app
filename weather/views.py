import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm
from django.conf import settings
from cities_light.models import City as CityLight


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + settings.WEATHER_API

    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            response = requests.get(url.format(city_name))

            city_light = CityLight.objects.filter(name=city_name.capitalize()).first()

            if (response.status_code == 200) and city_light:
                form.save()
                return redirect('/')
            return redirect('/')

    weather_data = []

    cities = City.objects.all()

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        
        if 'main' in city_weather:
            weather = {
                'city': city.name.capitalize(),
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
            }

            weather_data.append(weather)

    context = {
        'weather_data': weather_data,
        'form': form,
    }

    return render(request, 'weather/index.html', context)
