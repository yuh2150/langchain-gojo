import requests
import json
from requests.auth import HTTPBasicAuth

def geoCoding(location):
# URL of the API endpoint
    url = "https://map.local.goodjourney.io/api/mapProvider/geoCoding"

    # Parameters for the request
    params = {
        "address": {location},
        "channel": "chatbot"
    }

    # Sending the GET request
    response = requests.get(url, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        lat = data["results"][0]["geometry"]["location"]["lat"]
        lng = data["results"][0]["geometry"]["location"]["lat"]
        address = data["results"][0]["formatted_address"]
        print(lat, lng , address)
        return lat , lng , address
    else:
        print(f"Error: {response.status_code}")
        return None, None, None