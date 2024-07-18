import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm
from django.conf import settings
from cities_light.models import City as CityLight
from django.contrib import messages


def weather_dict(city):
    weather = {
        'city_id': city.id,
        'city': city.name.capitalize(),
        'temperature': city.temperature,
        'description': city.description,
        'icon': city.icon,
    }
        
    return weather


def index(request):
    url = settings.WEATHER_API_URL + settings.WEATHER_API

    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            response = requests.get(url.format(city_name))

            city_light = CityLight.objects.filter(name=city_name.capitalize()).first()

            in_cities = City.objects.filter(name__icontains=city_name)

            if (response.status_code == 200) and city_light and not in_cities:
                form.save()
                messages.success(request, f'{city_name.capitalize()} was added')
                return redirect('/')
            else:
                messages.warning(request, 'Incorrect city name!')
                return redirect('/')

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        if city.time_delta():
            city_weather = requests.get(url.format(city.name)).json()
            
            if 'main' in city_weather:
                city.temperature = city_weather['main']['temp']
                city.description = city_weather['weather'][0]['description']
                city.icon = city_weather['weather'][0]['icon']
                city.save()

                weather = weather_dict(city)
                weather_data.append(weather)
        else:
            weather = weather_dict(city)
            weather_data.append(weather)

    context = {
        'weather_data': weather_data,
        'form': form,
    }

    return render(request, 'weather/index.html', context)


def add_city(request):
    pass


def remove_city(request, pk):
    city = get_object_or_404(City, id=pk)
    city_name = city.name.capitalize()
    city.delete()

    messages.success(request, f'{city_name} was removed')

    return redirect('/')
