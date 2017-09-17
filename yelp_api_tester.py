from yelpapi import YelpAPI
import pprint
import requests

import json

yelp_api = YelpAPI('w0Tplfadr2wTECOfR51acQ', 'qRLjgpc5UsdiDKSUvMuYJ9PUDLyvCGby7ncE8Yar6BhPiQXI22B8OeyAysB7hlk6')


def search_yelp(cuisine, z):

    response_restaurants = yelp_api.search_query(term=cuisine, location=z, sort_by='rating', limit=3)

    print response_restaurants['businesses'][0]['name'] + ',' + response_restaurants['businesses'][0]['display_phone']
    print response_restaurants['businesses'][1]['name'] + ',' + response_restaurants['businesses'][1]['display_phone']
    print response_restaurants['businesses'][2]['name'] + ',' + response_restaurants['businesses'][2]['display_phone']

    return response_restaurants

search_yelp('indian','52240')