import requests
from requests.auth import HTTPBasicAuth

def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data = {"grant_type": "password", "username": "admin", "password": "xxxxxxxx"}
    response = requests.post(token_url, data)
    resp_body = response.json()
    token_value = resp_body["access_token"]

    auth= { "Authorization": "Bearer " + token_value}
    url = "https://thetestingworldapi.com/api/StDetails/1104"
    
    response = requests.get(url, headers=auth)
    print(response.json())