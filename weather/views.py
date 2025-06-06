from django.shortcuts import render
import json 
import urllib.request

def index(request):
    data = {}
    city = ''
    error_message = None
    
    if request.method == 'POST':
        city = request.POST['city']
        try:
            # Try to load the API response
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5be464c2e0141838a8ec254ffbb4608f'
            ).read()
            json_data = json.loads(source)
            
            # Check if city is found
            if json_data.get('cod') != 200:
                error_message = "City doesn't exist. Please enter a valid city name."
            else:
                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                    
                    "temp": "{:.2f} °C".format(json_data['main']['temp'] - 273.15),


                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                }
        except Exception as e:
            error_message = "City doesn't exist. Please enter a valid city name."

    return render(request, 'index.html', {'city': city, 'data': data, 'error_message': error_message})
