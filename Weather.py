
# coding: utf-8

# In[8]:

from weather import Weather
weather = Weather()
location= input()
location = weather.lookup_by_location(location)
condition = location.condition()
highTemp=location.atmosphere()
wind=location.wind()
temp=location.condition()
print ('Temperature: ' +temp['temp']+'F')
print ('Condition: ' +condition['text'])
print ('Wind Speed: '+wind['speed'] + 'kph')
print ('Humidity: ' + highTemp['humidity']+'%')


