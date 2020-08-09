import requests
import json
import os

# yelp api business search endpoint
def business_search(address):
    api_key = os.environ.get('api_key')
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'restaurants', 'radius': 1609, 'location': address}
    
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

# Sign into with firebase authetication
def sign_in(email, password):
    web_api_key = os.environ.get('fb_web_key')
    request_ref = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={web_api_key}"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    return request_object.status_code