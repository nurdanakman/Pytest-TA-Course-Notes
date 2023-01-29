from pathlib import Path
import requests
import json

base_url = "https://thetestingworldapi.com"

def test_add_new_data():
    global id
    url = base_url + "/api/studentsDetails"

    #read input json file
    file= open(Path(__file__).parent /"payloads"/'new_student_data.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)

    response = requests.post(url, payload)
    resp_body = response.json()

    id = resp_body["id"]

def test_get_details():
    url = base_url + "/api/studentsDetails/" + str(id)

    resp= requests.get(url)
    resp_body = resp.json()
    print(resp_body)

    assert resp_body["data"]["id"] == id