from pathlib import Path
import requests
import json
import pytest

base_url = "https://thetestingworldapi.com"


def test_add_student_data():
    url = base_url + "/api/studentsDetails"
    
    #read input json file
    file= open(Path(__file__).parent /"payloads"/'new_student_data.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)

    resp_body = requests.post(url, payload)
    print(resp_body.json())


def test_update_student_data():
    url = base_url + "/api/studentsDetails/4179689"

    #read input json file
    file= open(Path(__file__).parent /"payloads"/'updated_student_data.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)

    resp= requests.post(url, payload)
    resp_body = resp.json()
    print(resp_body)

    assert resp_body["first_name"] == "Nurdan1"


def test_fetch_student_details():
    url = base_url + "/api/studentsDetails/4179717"

    resp= requests.get(url)
    resp_body = resp.json()
    print(resp_body)

    assert resp_body["data"]["id"] == 4179717


@pytest.mark.skip
def test_delete_student():
    url = base_url + "/api/studentsDetails/4179689"

    resp= requests.delete(url)
    resp_body = resp.json()
    print(resp_body)