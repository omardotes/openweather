from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm
 # Create your views here.

def show_map(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6a6c63f4945f50812a8eb9efa5d57f31'
    cities = City.objects.all() #return all the cities in the database
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'country': city_weather['sys']['country'],
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'].capitalize(),
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data}

    return render(request, 'api.html', context) #returns the index.html template


        

