import requests
import json
import os

# yelp api business search endpoint
def business_search(address):
    api_key = os.getenv('api_key')
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'restaurants','radius':1609,'location':address}
    
    req=requests.get(url, params=params, headers=headers)
    
    # store json into data
    data = req.json()
    
    # Create empty restaurant array
    restaurant_array = []

    # For each business in the json array
    for restaurant in data['businesses']:

        # Insert the restaurant url into the array
        restaurant_array.append(restaurant['url'])
    return restaurant_array


