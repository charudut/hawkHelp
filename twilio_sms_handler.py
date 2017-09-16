"""
Python code to handle SMS queries sent to (515)800-2016
This is part of hawkHelp project done at University of Iowa Hackathon 2017
"""

from flask import Flask, request
from twilio import twiml
 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print message_body

    message_body_array = []
    message_body_array = message_body.split()
    #print message_body_array[0]
    #print message_body_array[1]
    #print message_body_array[2]

    if len(message_body_array) < 3:

        if message_body in ["list", "List"]:
            resp1 = twiml.Response()
            resp1.message('Menu Options:\n'
                     'Food\n'
                     'Movie\n'
                     #'Weather\n'
                     '\n'
                     'Reply back with a selection. For e.g. "food"')
            return str(resp1)

        if message_body in ["food", "Food"]:
            resp2 = twiml.Response()
            resp2.message('Select cuisine and location.\n'
                      'e.g. If you are in the mood for Chinese in Iowa City, reply back "food chinese 52240"')
            return str(resp2)

        if message_body in ["movie", "Movie"]:
            resp3 = twiml.Response()
            resp3.message('Select genre and location.\n'
                      'e.g. If you are in the mood for Logan in Iowa City, reply back "movie action 52240"')
            return str(resp3)

        else:
            respFirst = twiml.Response()
            respFirst.message('Hello {}, \n'
                     'Thank you for contacting hawkHelp. \n'
                     'Reply "list" to get started.'.format(number))
            return str(respFirst)

    else:
        if message_body_array[0] == 'food':
            resp_adv1 = twiml.Response()
            resp_adv1.message('working on yelp integration')
            return str(resp_adv1)

        if message_body_array[0] == 'movie':
            resp_adv2 = twiml.Response()
            resp_adv2.message('working on IMDB integration')
            return str(resp_adv2)
 
if __name__ == '__main__':
    app.run()