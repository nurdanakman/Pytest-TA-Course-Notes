from pathlib import Path
import requests
import json

base_url = "https://thetestingworldapi.com"

def test_add_new_data():
    url = base_url + "/api/studentsDetails"

    #read input json file
    file= open(Path(__file__).parent /"payloads"/'new_student_data.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)

    response = requests.post(url, payload)
    resp_body = response.json()

    id = resp_body["id"]


    url2 = base_url + "/api/technicalskills"

    #read input json file
    file= open(Path(__file__).parent /"payloads"/'technical_data.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)
    payload["id"] = id
    payload["st_id"] = id

    response = requests.post(url2, payload)
    resp_body = response.json()
    print(resp_body) 
