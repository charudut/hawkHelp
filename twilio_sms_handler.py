"""
Python code to handle SMS queries sent to (515)800-####
This is part of hawkHelp project done at University of Iowa Hackathon 2017
"""

from flask import Flask, request
from twilio import twiml
from weather import Weather
from yelpapi import YelpAPI

app = Flask(__name__)

yelp_api = YelpAPI('w0Tplfadr2wTECOfR51acQ', 'qRLjgpc5UsdiDKSUvMuYJ9PUDLyvCGby7ncE8Yar6BhPiQXI22B8OeyAysB7hlk6')

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    # print message_body

    message_body_array = []
    message_body_array = message_body.split()
    # print message_body_array[0]
    # print message_body_array[1]
    # print message_body_array[2]

    # a = query_api('Indian', '60609')

    if len(message_body_array) < 3:

        if message_body in ["list", "List"]:
            resp1 = twiml.Response()
            resp1.message('Menu Options:\n'
                          'Food\n'
                          'Doctor\n'
                          'Weather\n'
                          '\n'
                          'Reply back with a selection. For e.g. "food" if you\'re hungry')
            return str(resp1)

        if message_body in ["food", "Food"]:
            resp2 = twiml.Response()
            resp2.message('Select cuisine and location.\n'
                          'e.g. If you\'re in the mood for Chinese in 52240(Iowa City), reply "food chinese 52240"')
            return str(resp2)

        if message_body in ["doctor", "Doctor"]:
            resp3 = twiml.Response()
            resp3.message('What speciality are you looking for? And what\'s your Zipcode?\n'
                          'e.g. To find a neurology specialist in 52240(Iowa City), reply "doctor neurology 52240"')
            return str(resp3)

        if message_body in ["weather", "Weather"]:
            resp4 = twiml.Response()
            resp4.message('What is your Zipcode?\n'
                          'e.g. If you need weather info for 52240(Iowa City), reply back "weather forecast 52240"')
            return str(resp4)

        else:
            resp_first = twiml.Response()
            resp_first.message('Hello {}, \n'
                               'Thank you for contacting hawkHelp. \n'
                               'Reply "list" to get started.'.format(number))
            return str(resp_first)

    else:
        if message_body_array[0] in ["food", "Food"]:
            resp_adv1 = twiml.Response()
            r1, r2, r3 = search_yelp(message_body_array[1], message_body_array[2])
            master_response_food = r1 + '\n' + r2 + '\n' + r3
            resp_adv1.message(master_response_food)
            return str(resp_adv1)

        if message_body_array[0] in ["doctor", "Doctor"]:
            resp_adv2 = twiml.Response()
            d1, d2, d3 = search_yelp(message_body_array[1], message_body_array[2])
            master_response_food = d1 + '\n' + d2 + '\n' + d3
            resp_adv2.message(master_response_food)
            return str(resp_adv2)

        if message_body_array[0] in ["weather", "Weather"]:
            resp_adv3 = twiml.Response()
            #print message_body_array[2]
            response_weather = get_weather(message_body_array[2])
            #print response_weather
            resp_adv3.message(response_weather)
            return str(resp_adv3)

        if message_body[0] not in ["food", "Food", "movie", "Movie", "weather", "Weather"]:
            resp_adv_err = twiml.Response()
            resp_adv_err.message('We\'re sorry, but this is not a valid option.\n'
                                 'Feedback is appreciated! hello@hawkhelp.net\n'
                                 'Reply "list" to get started.')
            return str(resp_adv_err)


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

    weather_resp = "Forecast for today is " + condition['text'] + ". " + "\nTemperature: " + condition['temp'] + " F" + "\nWind Speed: " + wind['speed']+" kmph" + "\nhumidity: " + atmosphere['humidity']+"%"
    return weather_resp


def search_yelp(cuisine, z):

    response_restaurants = yelp_api.search_query(term=cuisine, location=z, sort_by='rating', limit=3)

    res1yelp = response_restaurants['businesses'][0]['name'] + ', ' + response_restaurants['businesses'][0]['display_phone']
    res2yelp = response_restaurants['businesses'][1]['name'] + ', ' + response_restaurants['businesses'][1]['display_phone']
    res3yelp = response_restaurants['businesses'][2]['name'] + ', ' + response_restaurants['businesses'][2]['display_phone']

    return res1yelp, res2yelp, res3yelp


if __name__ == '__main__':
    app.run()
