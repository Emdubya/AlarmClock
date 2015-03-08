#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import decimal

#change the weather to your city and 'metric' to 'imperial' for fahrenheit
request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?id=5992996&units=metric')
#request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?q=NYC&units=metric')

try:
    weather_api = urllib2.urlopen(request)
    response = weather_api.read()
    response_dictionary = json.loads(response)

    current = response_dictionary['main']['temp']
    current_low = response_dictionary['main']['temp_min']
    current_high = response_dictionary['main']['temp_max']
    conditions = response_dictionary['weather'][0]['description']

    current = round(current,1)
    current_low = round(current_low,1)
    current_high = round(current_high,1)
    #print current
    #print current_low
    #print current_high
    #print conditions

    # reads current weather
    wtr = 'Weather conditions for today are ' + str(conditions) + ' with a current temperature of ' + str(current)
except urllib2.HTTPError, e:
    wtr = 'Failed to connect to Open Weather Map.  '
except urllib2.URLError, e:
    wtr = 'Failed to connect to Open Weather Map.  '
except Exception:
    wtr = 'Failed to connect to Open Weather Map.  '

# print wtr

request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?id=5992996&units=metric&cnt=1')
#request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?q=NYC&units=metric&cnt=1')

try:
    forecast_api  = urllib2.urlopen(request_2)
    response_2 = forecast_api.read()
    response_2_dictionary = json.loads(response_2)

    todays_low = response_2_dictionary['list'][0]['temp']['night']
    todays_high = response_2_dictionary['list'][0]['temp']['day']

    todays_low = round(todays_low,1)
    todays_high = round(todays_high,1)

    #print todays_low
    #print todays_high

    # reads today’s forecast weather
    frc = ' with a low of ' + str(todays_low) + ' and a high of ' + str(todays_high) + '.  '

except urllib2.HTTPError, e:
    frc = 'Failed to connect to Open Weather Map.  '
except urllib2.URLError, e:
    frc = 'Failed to connect to Open Weather Map.  '
except Exception:
    frc = 'Failed to connect to Open Weather Map.  '

# print frc
