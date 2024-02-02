from django.shortcuts import render,HttpResponse
import requests
import json
from . import main

# Create your views here.
def home(request):
   
    city = request.POST.get('city')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={main.api_key}"
    response = requests.get(url)
    # icon = icon

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temperature = round(temp - 273.15 , 2)
        desc = data['weather'][0]['description']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        icon = data['weather'][0]['icon']  
        
    context = {
        'city':city,
        'temperature':str(temperature) +' '+'°C',
        'description':desc,
        'icon':icon,
        'wind':str(wind) + ' '+ 'km/h',
        'humidity':str(humidity) + '%',

    }

    return render(request,'weather_app/index.html',context=context)




