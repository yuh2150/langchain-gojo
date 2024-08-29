import requests
import json
from requests.auth import HTTPBasicAuth


def getQuotes():
    url = "https://dispatch.local.goodjourney.io/api/demand/v1/quotes"

    payload = json.dumps({
        "pickupDateTime": "2024-08-19T12:06:14Z",
        "pickup": {
            "latitude": 16.5594929,
            "longitude": 108.1502167,
        },
        "destination": {
            "latitude": 16.5594929,
            "longitude": 108.2117436,
        },
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbGVldElkIjoieWVsbG93IiwidGhpcmRQYXJ0eSI6IlZpbmNlbnQgQVBJIiwiYXBwTmFtZSI6IlZpbmNlbnQgQVBJIiwiX2lkIjoiNjU5NzgwMjQ1YTNmMmI0YzAyOGU1ZjlkIiwiaWF0IjoxNzI0MDQwNjE0LCJleHAiOjE3MjQwNDQyMTQsImF1ZCI6ImF1dGguZ29qby5nbG9iYWwifQ.4b_JAQh-lMQ3dxzb61L-QXqYvRxsymKAKokNroQ8iSQ'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    
lat , lng , address = geoCoding("03 le dinh ly , da nang")

print(lat)