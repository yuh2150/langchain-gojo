import requests
import json

url = "https://dispatch.local.goodjourney.io/api/demand/v1/bookings"
def Bookings():
    payload = json.dumps({
    "quoteId": "356ab316-0cc6-44ca-bcc0-fa134c01667d",
    "passenger": {
        "title": "Mr",
        "phone": "+120517347",
        "firstName": "Daid",
        "lastName": "James"
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbGVldElkIjoieWVsbG93IiwidGhpcmRQYXJ0eSI6IlZpbmNlbnQgQVBJIiwiYXBwTmFtZSI6IlZpbmNlbnQgQVBJIiwiX2lkIjoiNjU5NzgwMjQ1YTNmMmI0YzAyOGU1ZjlkIiwiaWF0IjoxNzI0MDQwNjE0LCJleHAiOjE3MjQwNDQyMTQsImF1ZCI6ImF1dGguZ29qby5nbG9iYWwifQ.4b_JAQh-lMQ3dxzb61L-QXqYvRxsymKAKokNroQ8iSQ'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.request.url)
    print(response.text)