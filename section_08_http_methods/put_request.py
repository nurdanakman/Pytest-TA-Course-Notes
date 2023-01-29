import requests #intall request package
import json # install
import http
from pathlib import Path

#pip list -> list all packages
# put update resource

base_url="http://reqres.in"

#read input json file
file= open(Path(__file__).parent /'create_user_update.json', 'r')
json_input = file.read()
payload = json.loads(json_input)

#POST request
response=requests.post(base_url + "/api/users/2", payload)
assert response.status_code == http.client.OK

#response header
print(response.headers.get("Date"))

#response body field
json_response = json.loads(response.text)
print(json_response["data"]["id"])
