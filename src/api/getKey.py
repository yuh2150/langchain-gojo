import requests
import json
from requests.auth import HTTPBasicAuth


def getKey():
    url = "https://dispatch.local.goodjourney.io/api/demand/oauth/token"

    username ='ck-0a003ed2bf354cdcf73b5f98edab77f2'
    password = 'sk-47279af8d764362a25e00c87e5127f67dcf39e5aa8952f4eb4c4d9ac518bf904'

    payload = json.dumps({
    })

    response = requests.get(url, headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }, data=payload, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()
        # Extract the access_token
        access_token = response_json.get("access_token")
        print(access_token)
        return access_token
    else:
        print(f"Error: {response.status_code}")
        return None
