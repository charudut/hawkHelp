from weather import Weather

def get_weather(zipcode):
    my_weather = Weather()
    location = my_weather.lookup_by_location(zipcode)
    condition = location.condition()
    atmosphere=location.atmosphere()
    wind=location.wind()
    temp=location.condition()

    climate=dict()
    climate={'Wind Speed ':wind ['speed']}
    climate['Temperature']= condition['temp']
    climate['Humidity']= atmosphere['humidity']
    climate['Condition']= condition['text']

    weather_resp = "Forecast for today is " + condition['text'] + ". " + "\nTemperature: " + condition['temp'] + "\nWind Speed: " + wind['speed'] + "\nhumidity: " + atmosphere['humidity']
    return weather_resp

get_weather(52240)