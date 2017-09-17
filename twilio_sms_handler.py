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
                          'Movie\n'
                          'Weather\n'
                          '\n'
                          'Reply back with a selection. For e.g. "food" if you\'re hungry')
            return str(resp1)

        if message_body in ["food", "Food"]:
            resp2 = twiml.Response()
            resp2.message('Select cuisine and location.\n'
                          'e.g. If you are in the mood for Chinese in Iowa City, reply back "food chinese 52240"')
            return str(resp2)

        if message_body in ["movie", "Movie"]:
            resp3 = twiml.Response()
            resp3.message('What is your Zipcode?\n'
                          'e.g. If you are in the mood for Logan in Iowa City, reply back "movie action 52240"')
            return str(resp3)

        if message_body in ["weather", "Weather"]:
            resp4 = twiml.Response()
            resp4.message('Select Value and Zipcode?\n'
                          'e.g. If you need temperature info for Iowa City, reply back "weather forecast 52240"')
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
            master_response_food = r1 + r2 + r3
            resp_adv1.message(master_response_food)
            return str(resp_adv1)

        if message_body_array[0] in ["movie", "Movie"]:
            resp_adv2 = twiml.Response()
            resp_adv2.message('working on IMDB integration. Updates to follow soon')
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
            resp_adv_err.message('We\'re sorry, but this option is not implemented yet.\n'
                                 'Feedback is appreciated! hello@hawkhelp.net')
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

    weather_resp = "Forecast for today is " + condition['text'] + ". " + "\nTemperature: " + condition['temp'] + "F" + "\nWind Speed: " + wind['speed']+"kmph" + "\nhumidity: " + atmosphere['humidity']+"%"
    return weather_resp


def search_yelp(cuisine, z):

    response_restaurants = yelp_api.search_query(term=cuisine, location=z, sort_by='rating', limit=3)

    res1yelp = response_restaurants['businesses'][0]['name'] + ',' + response_restaurants['businesses'][0]['display_phone']
    res2yelp = response_restaurants['businesses'][1]['name'] + ',' + response_restaurants['businesses'][1]['display_phone']
    res3yelp = response_restaurants['businesses'][2]['name'] + ',' + response_restaurants['businesses'][2]['display_phone']

    return res1yelp, res2yelp, res3yelp


if __name__ == '__main__':
    app.run()
