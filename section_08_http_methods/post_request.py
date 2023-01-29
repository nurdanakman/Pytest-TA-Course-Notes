import requests #intall request package
import json # install
import http
from pathlib import Path

#pip list -> list all packages
# post create new

base_url="http://reqres.in"

#read input json file
file= open(Path(__file__).parent /'create_user.json', 'r')
json_input = file.read()
payload = json.loads(json_input)

#POST request
response=requests.post(base_url + "/api/users", payload)
assert response.status_code == http.client.OK

#response header
print(response.headers.get("Date"))

#response body field
json_response=json.loads(response.text)
print(json_response)
print(json_response["page"])

